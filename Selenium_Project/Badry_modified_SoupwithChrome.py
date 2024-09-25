from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import os , time

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





# try:
#     try:
#         driver = webdriver.Edge(executable_path="Edge.exe")
#     except:
#         driver = Edge(executable_path=EdgeChromiumDriverManager().install())
# except Exception as E:
#     print(E)
#     quit()


driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

html = driver.page_source
soup = BeautifulSoup(html,features="html.parser")
# testElement = wait("button" ,"aria-label" , "Search with your voice" , 0)
testElement = wait("button" ,"class" , "yt-spec-button-shape-next" , 1)
print(testElement)
print(get_xpath(testElement))
# Keep the browser open for observation
input("Press Enter to close this browser...")
    
driver.quit()



'''

button = wait("button" ,"class" , "cdx-button cdx-search-input__end-button" , 0)
print(button)

print(get_xpath(button))


quit()
print(button.parent.name)
print(find_parent_rank(button.parent))




print(button.parent.parent.name)
print(find_parent_rank(button.parent.parent))

print(button.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent))

print(button.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent.parent.parent.parent.parent))

print(button.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.name)
print(find_parent_rank(button.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent))

'''

'''
In BeautifulSoup, when you encounter the parent name as "[document]", 
it means that the parent of the element is the root of the parsed document. 
This happens when the element is a direct child of the BeautifulSoup object itself, 
which represents the entire HTML document.
'''

#print(get_xpath(button))

