from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import os , time


from selenium.webdriver.common.keys import Keys
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
driver.get('https://www.instgram.com/')
time.sleep(10)
username_field = driver.find_element(By.NAME, "username")

    
for letter in "bbelal.ali":
    username_field.send_keys(letter)  # Send each letter
    time.sleep(0.1)  # Delay between letters

password_field = driver.find_element(By.NAME, "password")
for letter in "Bolbol00curt":
    password_field.send_keys(letter)  # Send each letter
    time.sleep(0.1)  # Delay between letters
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()  # Click the Log In button
time.sleep(10)
driver.get(f"https://www.instagram.com/hesham_262/")
time.sleep(10)
# print("Before Post")
# time.sleep(5) 
# html = driver.page_source
# soup = BeautifulSoup(html,features="html.parser")
# # testElement = wait("button" ,"aria-label" , "Search with your voice" , 0)
# testElement = wait("div" ,"role" , "button" , 0)
# print(testElement)
# print(get_xpath(testElement))
# time.sleep(10) 
most_recent_post = driver.find_element(By.XPATH, "//div[contains(@class, 'aagw')]") # Working # message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working

# Click on the most recent post
most_recent_post.click()

# Wait to see the post after clicking
time.sleep(5)  # Adjust time as needed for observation

print("After Post")
time.sleep(5) 
current_url = driver.current_url
print("Current URL:", current_url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html,features="html.parser")

# testElement = wait("div" ,"class" , "x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81" , 0)
testElement = wait("svg" ,"aria-label" , "Like" , 0)

print(testElement)
likePAth = get_xpath(testElement)
print("original svg like path")
print(likePAth)
desired_Like_xpath = likePAth.rsplit("/", 3)[0]  
print("desired like path")
print(desired_Like_xpath)
time.sleep(5) 
# try:
#     driver.find_element(By.XPATH, likePAth).click()
# except:
#     print("Not Clickable")

# try:
#     driver.find_element(By.XPATH, likePAth)

# except:
#     print("Not Enter")


# xx = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div") # Working , Correct Like Path 
xx = driver.find_element(By.XPATH, desired_Like_xpath)
print("Double Click")
time.sleep(5)
xx.click()
xx.click()
time.sleep(5)

# print("FINALE")
# time.sleep(20)
# xx = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div")
# time.sleep(5)
# xx.click()
# time.sleep(5)




# print("Using Bad Method")
# time.sleep(15) 
# driver.get(current_url)
# time.sleep(10)
# html = driver.page_source
# soup = BeautifulSoup(html,features="html.parser")
# # testElement = wait("button" ,"aria-label" , "Search with your voice" , 0)
# testElement = wait("div" ,"role" , "button" , 0)
# print(testElement)
# print(get_xpath(testElement))
# time.sleep(5) 
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

