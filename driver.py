from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
import pandas as pd

def google_search(location):
    """ Webscrapes data from google travel of your destination
    
    Params:
    location: the destination of your choice
    """
    text = location

    driver = webdriver.Chrome()
    driver.get('https://google.com/travel')

    driver.maximize_window()
    time.sleep(5)

    search = driver.find_element_by_id("oA4zhb")
    search.send_keys(text)
    search.send_keys(Keys.RETURN)

    #time.sleep(5)
    driver.implicitly_wait(10)
    #submit_button = driver.find_element_by_xpath('//*[@id="ow3"]/div[3]/div[2]/div/div[3]/card-carousel/div/div/a')
    submit_button = driver.find_element_by_class_name("rgrDvf")
    submit_button.click()

    url = driver.current_url
    categories = driver.find_elements_by_class_name("VfPpkd-RLmnJb")

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html5lib')

    cats = []
    for span in soup.findAll('span', attrs = {'class': 'veMtCf fzaxze'}):
        s = span.get_text()
        cats.append(s)

    categories = driver.find_elements_by_class_name("VfPpkd-RLmnJb")

    names = []
    descriptions = []
    ratings = []
    reviews = []
    genres = []

    urls = []
    for category in categories:
        time.sleep(5)

        if category != categories[-1]:
            category.click()
            url = driver.current_url
            urls.append(url)
        else:
            url = driver.current_url
            urls.append(url)

    urls.remove(urls[0]) # remove the first link        

    counter = 0
    for link in urls:
        time.sleep(5)
        
        driver.get(link)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html5lib')    

        for div in soup.findAll('div', attrs = {'class': 'GwjAi'}):

            try:
                name = div.find('div', attrs = {'class': 'skFvHc YmWhbc'}).get_text()
                description = div.find('div', attrs = {'class': 'nFoFM'}).get_text()
                rating = div.find('span', attrs = {'class':'KFi5wf'})
                review = div.find('span', attrs = {'class':'jdzyld'})
                genre = cats[categories.index(categories[counter])]

            except:
                pass

            names.append(name)
            descriptions.append(description)
            ratings.append(rating.text if rating else "N/A")
            reviews.append(review.text if review else "N/A")
            genres.append(genre)

        counter +=1

    driver.close()

    df = pd.DataFrame({'Attractions':names,'Descriptions':descriptions, 'City': text, 
                   'Ratings': ratings, 'Reviews': reviews, 'Genres': genres})
    
    return df
