import requests
from bs4 import BeautifulSoup
import webbrowser


def main():
    request = get_link()
    url, soup = get_soup(request)
    web_open(url)
    links_find(soup)


def get_link():
    a = "https://en.wikipedia.org/wiki/Special:Random"
    request = requests.get(a)
    return request


def get_soup(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    url = 'https://en.wikipedia.org/wiki/%s' %title
    return url, soup
    

def web_open(url):  
    webbrowser.open(url)


def links_find(soup):
    links_list = soup.find_all("a")
    for link in links_list:
        if "href" in link.attrs:
            print(str(link.attrs["href"]))


if __name__ == "__main__":
    main()
