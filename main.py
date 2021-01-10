import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import urllib


start_link = "https://en.wikipedia.org/wiki/Special:Random"
target_link = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = []

def main():
    PATH = input("Insert the absolute path to your Chromedriver: \nOr download it on https://chromedriver.chromium.org/downloads.")
    driver = driver_set(PATH)
    driver.get(start_link)
    my_counters = {"total": 1, "reset": 0}
    while driver.current_url != target_link:  
        first_link = links_find(driver.current_url)
        try:
            click_link = driver.find_element_by_xpath('//a[@href="'+first_link+'"]')
            click_link.click()
            if first_link in article_chain:
                print("Sorry, you are in loop.")
                my_counters["reset"] += 1
                driver.get(start_link)
            my_counters["total"] += 1
            article_chain.append(first_link)
        except: 
            print("Sorry, there is no link.")
            my_counters["reset"] += 1
            driver.get(start_link)
    print("You found Philosophy after {} tries and {} restarts.".format(my_counters["total"], my_counters["reset"]))
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
    try:
        for element in content_div.find_all("p", recursive=False):
            if element.find("a", recursive=False):
                article_link = element.find("a", recursive=False).get('href')
                break
        if not article_link:
            return
        return article_link
    except: return


if __name__ == "__main__":
    main()
