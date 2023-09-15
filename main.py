from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

start_link = "https://en.wikipedia.org/wiki/Special:Random"
target_link = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_article_link(driver):
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for element in soup.select("#mw-content-text .mw-parser-output p a[href^='/wiki/']"):
            return "https://en.wikipedia.org" + element.get("href")
    except:
        pass
    return None

def configure_webdriver():
    options = webdriver.ChromeOptions()
    options.headless = True
    return webdriver.Chrome(options=options)

def link_check(restarts, total_attempts, article_chain, first_link, driver):
    if first_link:
        if first_link in article_chain:
            print("Sorry, you are in a loop.")
            restarts += 1
            driver.get(start_link)
            article_chain.clear()
        else:
            driver.get(first_link)
            article_chain.append(first_link)
        total_attempts += 1    
    else:
        print("Sorry, there is no link.")
        restarts += 1
        driver.get(start_link)
        article_chain.clear()
    return restarts, total_attempts

def main():
    restarts = 0
    total_attempts = 0
    article_chain = []
    driver = configure_webdriver()
    while driver.current_url != target_link:
        first_link = find_first_article_link(driver)
        restarts, total_attempts = link_check(restarts, total_attempts, article_chain, first_link, driver)   
    print(f"You found Philosophy after {total_attempts} tries and {restarts} restarts.")
    driver.quit()

if __name__ == "__main__":
    main()