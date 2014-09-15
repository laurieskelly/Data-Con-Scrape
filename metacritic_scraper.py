#!/usr/bin/env python

import requests
from dateutil import parser

from bs4 import BeautifulSoup
import bs4.element

url = 'http://www.metacritic.com/browse/movies/release-date/theaters/date'


def connection(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text)
    return soup


def scrape_metacritic_list_page(soup,movie_list):
    for release_type,mlist in get_modules(soup).items():
        for movie in mlist:
            try:
                m = parse_movie_li(movie)
            except:
                bad.append(movie)
                continue
            m['release_type']=release_type
            movie_list.append(m)
    return movie_list

def just_tags(thinglist):
    tags = [t for t in thinglist if isinstance(t,bs4.element.Tag)]
    return tags
    
def get_modules(soup):
    modules = soup.find_all(class_='product_condensed')
    module_dict = {}
    for mod in modules: 
        label = mod.find(class_='release_type_label').text
        movie_lis = just_tags(mod.find('ol').contents)
        module_dict[label]=movie_lis
    return module_dict
    
def parse_movie_li(li):
    title_div = li.find(class_='product_title')
    
    movie = {
        'title':title_div.text.strip(),
        'rel_url':title_div.find('a')['href'],
        'metascore_w':get_metascore_w(li.find(class_='metascore_w')),
        'release_date': get_release_date(li.find(class_='release_date').find(class_='data'))
    }
    #print movie,'\n'
    return movie
    
def get_metascore_w(div):
    try:
        score = div.text
    except:
        print 'no text in metascore div'
        return None
    try: 
        score = int(score)
    except: 
        pass
    return score
    
    
def get_release_date(div):
    try: 
        datestr = div.text
    except:
        return None
    try: 
        date = parser.parse(datestr)
    except:
        return datestr
    return date



if __name__ == '__main__':

    import pickle
    
    url = 'http://www.metacritic.com/browse/movies/release-date/theaters/date'
    soup = connection(url)    
    movie_list = scrape_metacritic_list_page(soup)

    with open('metacritic_scrape.pkl','wb') as outfile:
        pickle.dump(movie_list,outfile)

    # sanity check
    with open('metacritic_scrape.pkl','rb') as infile:
        print pickle.load(infile)
