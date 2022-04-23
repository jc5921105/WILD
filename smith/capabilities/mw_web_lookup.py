import requests, pdb, time
try: from bs4 import BeautifulSoup as bs
except: pass


URL = "https://www.merriam-webster.com/dictionary/"


def get_definitions(word):
    print('Getting URL')
    url = _gen_request_url(word)
    print('Getting Request')
    time.sleep(.1)
    req = _gen_request(url)
    print('Getting Soup')
    soup = _get_soup(req)
    print('Getting POS')
    pos = _get_pos(soup)
    print('Parsing Info')
    return _parse_info(pos)


def _gen_request_url(word):
    return "%s%s" % (URL,word)


def _gen_request(url):
    while True:
        tmp = None
        cout = 0
        try: tmp = requests.get(url,timeout=5)
        except:
            count += 1
            print('Trying again for word: %s' % url)
        if tmp: return tmp
        if count >=10: raise EOFError


def _get_soup(req):
    soup = bs(req.content, "lxml")
    return soup


def _get_pos(soup):
    #pos = soup.findAll("div", {"class": "vg"})
    pos = soup.findAll( "span", {"class": "dtText"})
    return pos


def _parse_info(pos):
    t_dict = {}
    for x in range(len(pos)):
        tmp =  pos[x].text
        tmp = tmp.replace(':','',1)
        tmp = tmp.strip()
        t_dict[str(x + 1)] = tmp
    return t_dict


if __name__ == '__main__':
    print(get_definitions('ice'))