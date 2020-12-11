import requests
from bs4 import BeautifulSoup
import webbrowser


while True:
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    url = 'https://en.wikipedia.org/wiki/%s' %title
    webbrowser.open(url)
    break
