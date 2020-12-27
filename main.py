import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import urllib

start_link = "https://en.wikipedia.org/wiki/Special:Random"
target_link = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_link]

def main():
    PATH = input("Insert the absolute path to your Chromedriver: \nOr download it on https://chromedriver.chromium.org/downloads.")
    driver = driver_set(PATH)
    driver.get(start_link)
    my_counter = 1
    while article_chain[-1] != target_link:   
        first_link = links_find(article_chain[-1])
        driver.get(first_link)
        if first_link in article_chain:
            first_link = start_link
            print("Sorry you are in loop")
        article_chain.append(first_link)
        my_counter += 1
    print("You found Philosophy after {} try".format(my_counter))
    driver.close()


def driver_set(PATH):
    driver = webdriver.Chrome(PATH) 
    return driver


def links_find(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(
        id="mw-content-text").find(class_="mw-parser-output")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link


if __name__ == "__main__":
    main()
