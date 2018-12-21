from datetime import *
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json, os
from lxml import html, etree
import requests

now = datetime.datetime.now()
string = now.strftime("%d-%b-%Y") + ".json"

print("NY Times Daily Crossword Puzzle crawler for CS461 Artificial Intelligence course.")
print("Fetching clues.")

def cluess():
    f = open(string, "w")
    page = requests.get('https://www.nytimes.com/crosswords/game/mini/')
    tree = html.fromstring(page.content)
    across = tree.xpath('//span[@class="Clue-label--2IdMY"]/text()')
    clues = tree.xpath('//span[@class="Clue-text--3lZl7"]/text()')
    a = ""

    now = datetime.datetime.now()
    a += '{\n\t"day" : "'
    a+=now.strftime("%A")
    a+='",\n\t"date" : "'
    a+=str(now.strftime("%b %d, %Y"))
    a+='",\n'

    for i in range(len(clues)):
        if('"' in clues[i] ):
            clues[i] = clues[i].translate(str.maketrans({'"': r'\"'}))
        if(i>4):
            if(i==5):
                a += '\t\t],\n\t"down": [\n'
                          
            a += '\t\t{"no": "'+across[i]+'", "text": "'+clues[i]+'"}'
            if(i!=9):
                a += ",\n"
            else:
                a+="\n"

        else:
            if(i==0):
                a += '\t"across": [\n'
                
            a += '\t\t{"no": "'+across[i]+'", "text": "'+clues[i]+'"}'
            if(i!=4):
                a += ",\n"
            else:
                a+="\n"

    a += "\t\t],"

    f.write(a)
    f.close
    print("Clues successfully fetched.")

def getPuzzle(driver):
    
    f = open(string, "a")
    # start to get puzzle
    sols = []
    tex = []
    driver.get("https://www.nytimes.com/crosswords/game/mini/")

    try:
        start_button = driver.find_element_by_class_name("buttons-modalButton--1REsR")
        start_button.click()
    except NoSuchElementException:
        try:
            driver.find_element_by_class_name("Toolbar-resetButton--1bkIx").find_element_by_tag_name("button").click()
        except:
            return None

    cellContainer = driver.find_element_by_css_selector('[data-group="cells"]')
    cells = cellContainer.find_elements_by_tag_name("g")

    x = 1
    y = 1

    for cell in cells:     
        try:
            text = cell.find_element_by_tag_name("text").text

            if text=="":
                tex.append(str(0))
            tex.append(text)
           
        except NoSuchElementException:
            tex.append(str(-1))

        if x % 5 == 0:
            y += 1
            x = 0
        x += 1
    
    #Solutions start from here
    solButton = driver.find_element_by_css_selector(".Toolbar-expandedMenu--2s4M4").find_elements_by_css_selector(".Tool-button--39W4J.Tool-tool--Fiz94.Tool-texty--2w4Br")[1]
    solButton.click()
    revealButton = solButton.find_elements_by_css_selector(".HelpMenu-item--1xl0_")[2]
    revealButton.click()
    button = driver.find_element_by_css_selector(".buttons-modalButtonContainer--35RTh").find_elements_by_css_selector(".buttons-modalButton--1REsR")[1]
    button.click()
    closeButton = driver.find_element_by_css_selector(".ModalBody-closeX--2Fmp7")
    closeButton.click()
    cellContainer = driver.find_element_by_css_selector('[data-group="cells"]')
    cells = cellContainer.find_elements_by_tag_name("g")

    x = 1
    y = 1

    for cell in cells:
        rect = cell.find_element_by_tag_name("rect")
        try:
            texts = cell.find_elements_by_tag_name('text')
           
            if len(texts) == 0:
                sols.append(str(-1))
            if len(texts) == 1:              
                sols.append(texts[0].text)
            if len(texts) == 2:
                sols.append(texts[1].text)

        except NoSuchElementException:
            pass

        if x % 5 == 0:
            y += 1
            x = 0
        x += 1

    x = 1
    y = 1

    while '' in tex:
        tex.remove("")

    foo = ""

    foo += '\n\t"cells" :  ['
    for ij in range(len(tex)):
        
        if len(tex)-1== ij:
            foobar = '"'+str(tex[ij])+'"],\n'
        else:
            foobar = '"'+str(tex[ij])+'",'
        foo += foobar   
        
    foo += '\t"answers": ['
    for ji in range(len(sols)):
        if len(sols)-1==ji:
            foo+= '"'+str(sols[ji])+'"]\n}'
        else:   
            foo+= '"'+str(sols[ji])+'",'

    f.write(foo)
    print("Grid successfully fetched.")

cluess()
seleniumDriver = webdriver.Chrome("/Users/caggri/Desktop/Archive/chromedriver")
print("Fetching grid")
getPuzzle(seleniumDriver)
seleniumDriver.close()
print(f"Crawling operation is done\nA JSON file is created with the name of {string}.")
