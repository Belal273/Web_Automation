print("Hello World")
# Feature Switch Account
#  TO_DO >> Switch by clicking log out not restarting browser 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Initialize the WebDriver (make sure to specify the correct executable path if necessary)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Open Instagram's main page
driver.get("https://www.instagram.com")

# Optional: maximize the window
driver.maximize_window()

# Wait for a few seconds to see the page
time.sleep(5)

# Locate the username input field and enter "bbelal.ali"
username_field = driver.find_element(By.NAME, "username")  # Update the selector if necessary
# username_field.send_keys("bbelal.ali")
# Type the username letter by letter
# "teampetssparkle"
# "petssparkle.02"

username = "petssparkle.009"
for letter in username:
    username_field.send_keys(letter)  # Send each letter
    time.sleep(0.2)  # Delay between letters

# Wait for a few seconds before password
time.sleep(3)

# Locate the password input field and enter "bolbol00curt"
password_field = driver.find_element(By.NAME, "password")  # Find the password input field
# password_field.send_keys("bolbol00curt")  # Enter the password
# Type the password letter by letter
# "teampetssparkleMK03"
# "sparkMK03"
mypassword = "petssparkle&1"

for letter in mypassword:
    password_field.send_keys(letter)  # Send each letter
    time.sleep(0.2)  # Delay between letters

# Wait for a few seconds before login
time.sleep(3)

# Locate the Log In button using the provided XPath and click it
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()  # Click the Log In button

# Keep the browser open
# input("Press Enter to go to client profile page ")  # Wait for user input

# Wait for a few seconds 
time.sleep(10)

#Navigate to client profile page
driver.get("https://www.instagram.com/mahmoud_m_samir/")

# Wait for a few seconds 
time.sleep(10)

# Locate the Follow button using the provided XPath and click it
# Locate the "Follow" button using a more general XPath


# Locate the "Follow" button using CSS Selector
follow_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # Working  




#TO_DO
# How to locate elments that have dynamic id and Xpath (using class for example )
# Better waiting time
# Error handlers



# Click the "Follow" button
follow_button.click()



# Wait for a few seconds
time.sleep(10)

####################################################################################################
# # role link
# # tabindex 0 
# # Locate the Message button using the provided XPath and click it
# # post = driver.find_element(By.CSS_SELECTOR, "div[role='img']") 

# # # # Click the "Message" button
# # post.click()

# # first_post =  driver.find_element(By.CSS_SELECTOR, "article a[href*='/p/']")
# # first_post.click()

# time.sleep(5)  # Allow time for the post to load
# driver.get("https://www.instagram.com")

# # Feature Switch Account
# #  TO_DO >> Switch by clicking log out not restarting browser 
# driver.quit()
# driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
# # Open Instagram's main page
# driver.get("https://www.instagram.com")
####################################################################################################

# Locate the Message button using the provided XPath and click it
message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']") 

# # Click the "Message" button
message_button.click()

# Wait for a few seconds
time.sleep(10)

# Locate the Send Message Textbox using the provided XPath and click it
message_txtBox = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']") 

# # Click the "Message" button
# message_txtBox.click()

marketing_message = """Hello there!
We hope you’re having a great day! 
We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
Would you like to learn more about our ambassador program?
| @petssparkle"""

marketing_message2 = """Hello there!
We hope you’re having a great day! 
We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
Would you like to learn more about our ambassador program? 
| @petssparkle"""

# message_txtBox.send_keys(marketing_message2)
for letter in marketing_message:
    message_txtBox.send_keys(letter)  # Send each letter
    time.sleep(0.2)  # Delay between letters

# Press the Enter key
message_txtBox.send_keys(Keys.RETURN)




# Keep the browser open
input("Press Enter to close the browser...")  # Wait for user input

# Close the browser when done
driver.quit()

# Close the browser
#driver.quit()




