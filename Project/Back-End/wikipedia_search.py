from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

# define punctuation
punctuations = '''0123456789çşığ!()-[]{};:'"\,<>./?@#$%^&*_~'''

def parse_google_selenium(clue, page=None):
    wikipedia_words = set()
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
    for elem in result_headers:
        for word in elem.text.split():
            wikipedia_words.add(word)

    sel_driver.close()
    return wikipedia_words

def wikipedia(clue, length=None, seleniumUsed=False):
    wikipedia_words = set()
    if seleniumUsed:
        wikipedia_words = parse_google_selenium(clue, page="wikipedia.com")
    else:
        clue = clue.replace(" ", "+")

        request = requests.get('https://www.google.com/search?q={}&as_pagesearch=dictionary.com&lr=lang_en'
        .format(clue))
        soup = BeautifulSoup(request.content, "html.parser")
        result_elements = soup.text

        for word in result_elements.split():
            wikipedia_words.add(word)


    # getting rid of from unnecessary chars
    mylist = []
    for word in wikipedia_words:
        no_punct = ""
        for char in word:
           if char not in punctuations:
               no_punct = no_punct + char
        no_punct.lower()
        mylist.append(no_punct)
    wikipedia_words = mylist

    # Process word list
    #wikipedia_words = self.clear_wikipedia_words(wikipedia_words)
    wikipedia_words = list(filter(lambda x: len(x) == length, wikipedia_words))
    print("Wikipedia Search \nWord Count: " + str(len(wikipedia_words)))
    return wikipedia_words

"""
search = "hunk of cheese"
length = 5
print(wikipedia(search,length))
"""
