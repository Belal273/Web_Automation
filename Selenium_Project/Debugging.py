import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
import os 
import time

# from selenium.webdriver.common.keys import Keys
import threading
import pandas as pd

global driver

def get_xpath(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)

def wait( type, x, y, element_no):
    global recover_flag
    global driver
    counter = 0
    while True:
        if counter == 150:
            os.system('cls')
            print("recovering")
            recover_flag = True
            return
        os.system('cls')
        print(counter)
        time.sleep(.5)
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")
            elem = soup.find_all(type, {x: y})
            if (len(elem) > 0):
                break
            counter = counter + 1
        except:
            os.system('cls')
            print("recovering")
            recover_flag = True
            return
    return elem[element_no]

def find_parent_rank(parent):
    if parent.parent:
        siblings = [sib for sib in parent.parent.children if sib.name == parent.name]
        return siblings.index(parent) + 1
    return 1  # If no parent, it is the only element, rank is 1

# driver = webdriver.Chrome()
# driver.get('https://www.instgram.com/')

# html = driver.page_source
# soup = BeautifulSoup(html,features="html.parser")
# # testElement = wait("button" ,"aria-label" , "Search with your voice" , 0)
# testElement = wait("button" ,"type" , "submit",0)
# print(testElement)
# print(get_xpath(testElement))
# # Keep the browser open for observation

driver = webdriver.Chrome()
def habl(ss):
    
    driver = ss
    driver.get('https://www.instgram.com/')

    html = driver.page_source
    soup = BeautifulSoup(html,features="html.parser")
    # testElement = wait("button" ,"aria-label" , "Search with your voice" , 0)
    testElement = wait("button" ,"type" , "submit",0)
    print(testElement)
    print(get_xpath(testElement))
    input("Press Enter to close this browser...")
    
    driver.quit()

try:
    habl(driver)
except:
    pass