from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

# define punctuation
punctuations = '''0123456789çşığ!()-[]{};:'"\,<>./?@#$%^&*_~'''

def parse_google_selenium(clue, page=None):
    google_words = set()
    sel_driver = webdriver.Chrome()
    sel_driver.get("https://www.google.com")
    bar = sel_driver.switch_to.active_element
    if page is None:
        bar.send_keys(clue)
    else:
        bar.send_keys(clue + " " + "page:" + page)

    bar.send_keys(Keys.ENTER)
    sel_driver.get(sel_driver.current_url + "&lr=lang_en")


    result_headers = sel_driver.find_elements_by_id("rso")
    for element in result_headers:
        for word in element.text.split():
            google_words.add(word)

    sel_driver.close()
    return google_words

def google(clue, length=None, seleniumUsed=False):
    google_words = set()
    if seleniumUsed:
        google_words = parse_google_selenium(clue)
    else:
        clue = clue.replace(" ", "+")

        request = requests.get('https://www.google.com/search?q={}&lr=lang_en'
        .format(clue))
        soup = BeautifulSoup(request.content, "html.parser")
        result_elements = soup.text

        for word in result_elements.split():
            google_words.add(word)


    # getting rid of from unnecessary chars
    mylist = []
    for word in google_words:
        no_punct = ""
        for char in word:
           if char not in punctuations:
               no_punct = no_punct + char
        no_punct.lower()
        mylist.append(no_punct)
    google_words = mylist

    # Process word list
    #google_words = self.clear_google_words(google_words)
    google_words = list(filter(lambda x: len(x) == length, google_words))
    print("Google Search \nWord Count: " + str(len(google_words)))
    return google_words

"""
search = "one end of a battery"
length = 5
print(google(search,length))
"""
