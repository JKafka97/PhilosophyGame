import requests
from bs4 import BeautifulSoup
import webbrowser
import random


def main():
    request = get_link()
<<<<<<< HEAD
    url = get_soup(request)
    web_open(url)
=======
    url, soup = get_soup(request)
    web_open(url)
    while "Philosophy" not in url:
        url, soup = links_find(soup)
        web_open(url)
>>>>>>> dev


def get_link():
    a = "https://en.wikipedia.org/wiki/Special:Random"
    request = requests.get(a)
    return request


def get_soup(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    url = 'https://en.wikipedia.org/wiki/%s' %title
<<<<<<< HEAD
    return url
=======
    return url, soup
>>>>>>> dev
    

def web_open(url):  
    webbrowser.open(url)


<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
def links_find(soup):
    rnd_num = random.randint(3,5)
    for link in (soup.findAll('a'))[rnd_num:]:
            try:
                if "." not in (list(link.get('href')))[-5:] :
                    next_link = link.get('href')
                    if "404" in next_link or "searchInput" in next_link or "org" in next_link:
                        continue
                    else: break
            except: continue
    url = "https://en.wikipedia.org//" + next_link
    getr = requests.get(url)
    soup = BeautifulSoup(getr.text, 'html.parser')
    return url, soup


if __name__ == "__main__":
    main()
>>>>>>> dev
