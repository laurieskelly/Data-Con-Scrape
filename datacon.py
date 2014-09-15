import pickle
from StringIO import StringIO
from PIL import Image


def make_datacon_facesheet(faces,nrows=7,ncols=5):
    #faces = iter(get_faces_from_sessions(raw_sessions))
    faces = iter(faces)
    with open('facesheet.md','w') as outfile:
        outfile.write('| . '*ncols + '|\n')
        outfile.write('|----'*ncols + '|\n')
    for row in range(nrows):
        row = '|'
        for col in range(ncols):
            row += '###%s  \n![](%s)'%faces.next()
    
    return table
    
def get_faces_from_sessions(raw_sessions):
    faces = []
    for session in raw_sessions:
        table = session.find('table')
        rows = table.find_all('tr')
        num_speakers = len(rows[1].find_all('img'))
        print 'speakers in this session: %i'%num_speakers
        
        for i in range(num_speakers):
            top_row = rows[0]
#            print top_row
            speaker = top_row.find_all('th')[i].text.strip()
            speaker = ' '.join(speaker.split())
            picture_src = rows[1].find_all('td')[i].find('img')['src']
            local_picture_src = save_speaker_picture(speaker,picture_src)
        
            faces.append((speaker,local_picture_src))
    return faces

def save_speaker_picture(speaker,picture_src):
    print 'retrieving picture for %s'%speaker
    r = requests.get(picture_src)
    i = Image.open(StringIO(r.content))
    filename = '_'.join(speaker.lower().split()) + '.jpg'
    filename = './img/'+filename

    with open(filename,'w') as outfile:
        i.save(filename,'JPEG')

    return filename

def connection(url):
    r = requests.get(url)
    soup = None
    if r.ok:
        soup = BeautifulSoup(r.text)
    else:
        print 'request unsuccessful with code %s'%response.status_code
    return soup

def connection_w_headers(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}
    r = requests.get(url,headers=headers)
    soup = None
    if r.ok:
        soup = BeautifulSoup(r.text,'html5lib')
    else:
        print 'request unsuccessful with code %s'%response.status_code
    return soup
