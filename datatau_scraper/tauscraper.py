import requests
import pickle
import urlparse
from datetime import datetime
from bs4 import BeautifulSoup

START_URL = 'http://www.datatau.com/'
PAGE_LIMIT = 10
RAW_PAGE_PICKLEFILE = 'data/tau_raw_pages.pkl'
TAU_DICT_PICKLEFILE = 'data/tau_item_dict.pkl' 

class TauCollection(object):

    def __init__(self,tau_dict={},raw_pages=[]):
        '''
        creates a new collection object with empty data attributes 
        existing ones can be loaded from pickles using 
        load_data_from_pickles()
        '''
        self.tau_dict=tau_dict
        self.raw_pages=raw_pages

    def scrape_datatau(self,append=True):
        '''
        main method. 
        specifying append=False means the scraper will create new pickles
        this would overwrite old pickles unless moved or the global names changed
        when append=True, previously collected items are updated rather than duplicated.

        checks for and loads archived data if exists, or 
        starts fresh if there are no pickles or append=False. 
        iterates through datatau pages, starting from the front page, until 
        there aren't any more pages (so far looks like 7 pages, 210 items).

        pickles results (self.tau_dict) and returns collection object 
        '''
        if append:
            self.load_data_from_pickles()

        soup_queue = self.fill_soup_queue()
 
        for i,page in enumerate(soup_queue):
            print 'processing page',str(i+1)
            self.process_page(page)

        self.pickle_me()

        return self


    def load_data_from_pickles(self,
                               dict_pkl=TAU_DICT_PICKLEFILE,
                               raw_pkl=RAW_PAGE_PICKLEFILE):

        '''
        looks for archived data pickles and loads them into the collection 
        object if they exist
        '''
        try:
            with open(dict_pkl,'rb') as inpickle:
                tau_dict = pickle.load(inpickle)
                msg = 'loaded tau item dict from pickle'
        except IOError:
            msg = 'could not load tau item dict pickle. creating new dict'
            tau_dict = {}

        self.tau_dict = tau_dict
        print msg

        try:
            with open(raw_pkl,'rb') as inpickle:
                raw_pages = pickle.load(inpickle)
                msg = 'loaded raw pages dict from pickle'

        except IOError:
            msg = 'could not load raw pages pickle. creating new archive'
            raw_pages = []
    
        self.raw_pages = raw_pages
        print msg

        return self

    def pickle_me(self):
        '''
        pickles the data in the collection. automatically does this at the end
        of the main method sequence. few options here -- assumes you'll be 
        appending to the same pickles continually. Archiving pickles in 
        case of snafus is upon the user. 

        TODO: this pickling and archiving logic is a little weak. I don't think the 
        raw archives should be managed in the same way as the main pickle dict.

        TODO: there is also nothing built yet to restore a dict from the 
        archived raw files.
        '''
        
        print 'pickling the data'
        with open(RAW_PAGE_PICKLEFILE,'wb') as outfile1:
            pickle.dump(self.raw_pages,outfile1)
        with open(TAU_DICT_PICKLEFILE,'wb') as outfile2:
            pickle.dump(self.tau_dict,outfile2)


    def fill_soup_queue(self):
        ''' 
        gets and soups the datatau pages for processing, starting at START_URL
        (datatau mainpage) and clicking next until there are no more pages or 
        until there are no more pages on datatau (7 in my experience), or until 
        there are PAGE_LIMIT pages in the queue. Well, maybe PAGE_LIMIT + 1. OBOE.

        returns list of soups for processing

        TODO: it makes more sense to pickle the raw files now, before processing
        starts and has the opportunity to fail!
        yep. that's the ticket. ...the pickle ticket.
        '''

        soup_queue = []
        print 'filling the queue'
        page = self.open_page(START_URL)

        for i in range(PAGE_LIMIT):
            soup_queue.append(page)
            next_url = self.find_next_url(page)
            if not next_url:
                break
            print 'next url:',next_url
            page = self.open_page(next_url)
        print 'soup queue full, queued %d pages'%len(soup_queue)
        return soup_queue


    def find_next_url(self,soup):
        '''
        takes a soup  
        returns the full url of the next page to parse,
        if this exists.
        '''

        try: 
            a = soup.find(text='More').find_parent()
        except AttributeError:
            print 'reached end of items'
            return None
        href = a['href']
        return urlparse.urljoin(START_URL,href)

    def open_page(self,url):
        '''
        takes a url. 
        calls connection() to request the page 
        returns the soup of the contents or None
        '''

        soup = self.connection(url)
        self.raw_pages.append((datetime.now(),url,soup.prettify()))
        return soup


    def connection(self,url):
        '''
        gets the url from open_page()
        tries to open the page  
        returns the soup of the page or None
        '''

        r = requests.get(url)
        if r.ok:
            soup = BeautifulSoup(r.content)
            return soup
        else:
            return None
            
    def process_page(self,page):
        ''' 
        takes a page and breaks it down to rows,
        then items, and then processed items.

        on successful complettion, collection object 
        has a happy dict full of datatau information 
        (new and updated items)
        '''
        print 'soup to rows'
        rows = self.fresh_page_to_rows(page)
        print 'rows to items'
        items = self.rows_to_items(rows)
        print 'processing items'
        return self.process_items(items)

    def fresh_page_to_rows(self,soup):
        '''
        takes a soup, returns all rows
        '''
        rows = soup.find('table').find_all('tr')[4:]
        return rows


    def rows_to_items(self,rows):
        ''' 
        takes a list of rows, discards uninteresting rows, and groups the remaining
        rows into the 30 "items" on the page

        more info, a.k.a. why this is kind of funky: 
        Datatau is pretty much one big table. Items are two rows, with one 
        spacer row in between. There are a few junk rows at the top and the bottom
        that we don't want. There are no divs or special classes that differentiate 
        the rows, really. So I'm doing it by counting. This is usually the second-dumbest
        way to do something, because parsing by counting is very fragile to small changes. 

        But I like to live dangerously... 

        And I couldn't think of something better at the moment... 
        '''

        items = []
        row_iterator = iter(rows)
        more = True
        while more:
            try:
                items.append([row_iterator.next(),row_iterator.next()])
                spacer = row_iterator.next()
            except StopIteration:
                more = False
        ## dump off the last one that is not an item
        end_thingie = items.pop()
        return items

    def process_items(self,items):
        ''' 
        takes a list of items.

        for each item:
        finds first the id of the item and creates a TauItem object
        checks if ID is already in the collection dictionary self.tau_dict
        parses the item
        adds it to dictionary or updates existing entry.
        
        '''
        for i,raw_item in enumerate(items):
            item_id = int(raw_item[1].find_all('a')[-1]['href'].split('=')[1])
            
            tau_item = TauItem(item_id,raw_item)
            
            tau_item.parse()

            if item_id in self.tau_dict.keys():
                print 'updating item:',item_id
                tau_item.update_entry(self)
            else:
                self.tau_dict[item_id]=tau_item.entry
        return self

class TauItem(object):

    def __init__(self,item_id,raw_item):
        self.id_ = item_id
        self.raw = raw_item

    def parse(self):
        '''
        parses the item and adds its data to the TauItem object as self.entry
        '''
        rank,arrow,title = self.raw[0].find_all('td')
        spacer,subtext = self.raw[1].find_all('td')

        try:
            domain = title.find('span').text.strip().replace('(','').replace(')','')
        except AttributeError:
            domain = 'datatau.com'

        entry = {
            'rank':[(datetime.now(),int(rank.text[:-1]))],
            'url':title.find('a')['href'],
            'title':title.find('a').text,
            'domain': domain,
            'score':[(datetime.now(),int(subtext.text.split()[0]))],
            'submitter':subtext.find('a').text,
            'submitted_ago_from_first_accessed':' '.join(subtext.text.split()[4:6]),
            'first_accessed': datetime.now(),
        }

        # not implemented
        # the submission date is first_accessed - submitted_ago_from_first_accessed
        # I am too lazy to parse it right now, and it can be created from the 
        # collected data at any time. 
        self.entry  = self.calculate_submission_date(entry)
        


    def update_entry(self,collection):
        '''
        if the id of the item is already a key in the tau_dict,
        the item is updated by adding tuples of the date and value
        to the things that change (rank and score).
        '''

        entry = collection.tau_dict[self.id_]
        entry['rank'].append(self.entry['rank'][0])
        entry['score'].append(self.entry['score'][0])
        return collection


    def calculate_submission_date(self,entry):
        ''' 
        not implemented
        '''
        entry['submission_date'] = 'submission date calculation not implemented'

        return entry


if __name__ == '__main__':

    collection = TauCollection()
    collecttion.scrape_datatau()
