# backend.py
import sys
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from frontend_Adv import Ui_MainWindow  # Import the frontend UI class
from PyQt5.QtWidgets import QMessageBox

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
import os 



class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Initialize file path
        self.file_path = None  # Initialize the file_path attribute
        self.num_of_accounts = 0
        self.current_username = None
        self.current_password = None
        self.browsers_data = []

        # Additional logic can go here
        self.setup_connections()
        # self.ui.Run_pushButton.clicked.connect(self.handle_Run_Button)# Way2: Connect object with function directly inside init
        
    def setup_connections(self):
        # Example: Connecting signals to slots
        self.ui.Browse_pushButton.clicked.connect(self.handle_browse_button_click) # Way1: Connect object with function inside setup connection
        self.ui.Run_pushButton.clicked.connect(self.handle_Run_Button) # Way2: Connect object with function directly inside init
        self.ui.Password_textEdit.setPlaceholderText("Enter your password") # TO_DO # Hide Password Characters
        self.ui.UserName_textEdit.setPlaceholderText("Enter your username") 
        self.ui.Add_pushButton.clicked.connect(self.handle_Add_Button) # If Add pushbutton is clicked go to handle_Add_Button function
        self.ui.Remove_pushButton.clicked.connect(self.handle_Remove_Button) # If Remove pushbutton is clicked go to handle_Remove_Button function
        self.ui.Check_pushButton.clicked.connect(self.handle_Check_Button) # If Check pushbutton is clicked go to handle_Check_Button function
        self.ui.Message_checkBox.stateChanged.connect(self.on_checkbox_state_changed)

    def on_checkbox_state_changed(self):
        if self.ui.Message_checkBox.isChecked()== True:
            print(self.ui.Message_checkBox.isChecked())  # Checkbox is checked

    def handle_Add_Button(self):
        # TO_DO # Feedback in Dialogue_textBrowser

        # Get the content of the text edits
        username = self.ui.UserName_textEdit.toPlainText().strip()
        password = self.ui.Password_textEdit.toPlainText().strip()
    
        # Check if both fields are not empty
        if username and password:
            self.ui.UserName_textEdit.clear()
            self.ui.Password_textEdit.clear()
            self.ui.Password_textEdit.setPlaceholderText("Enter your password") 
            self.ui.UserName_textEdit.setPlaceholderText("Enter your username") 
            # You can use the username and password variables here
            print(f"Username: {username}, Password: {password}")
            self.num_of_accounts = self.num_of_accounts + 1
            self.browsers_data.append({
            'username': username,
            'password': password,
            'profile': []
        }) 
        
            # Clear the text edits
            # self.ui.UserName_textEdit.clear()
            # self.ui.Password_textEdit.clear()
            
        else:
            # Show a warning message box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Both fields are required.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def handle_Remove_Button(self):
        if self.num_of_accounts > 0:
            self.num_of_accounts = self.num_of_accounts - 1
        
        if self.browsers_data:
            self.browsers_data.pop()
        

    def handle_Check_Button(self):
        print(f"Num of accounts : {self.num_of_accounts}")
        print("self.browsers_data")
        print(self.browsers_data)
        # TO_DO # Make it Remove all
        # self.browsers_data = []
        # self.num_of_accounts = 0
        # print("self.browsers_data After Clear All")
        # print(self.browsers_data)

    def handle_browse_button_click(self):
        # Logic for what happens when the button is clicked
        print("Browse Button clicked in backend!")
        # Open a file dialog to select a file
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
            "Select a File", "", "All Files (*);;Excel Files (*.xls *.xlsx)", options=options)
        
        if file_path:
            # Store the selected file path in the instance variable
            self.file_path = file_path
            # Display the selected file path (you can also set it to a text field, if desired)
            print("Selected file:", file_path)
            self.ui.Path_textBrowser.setText(file_path)  # Assuming you have a QTextBrowser t
    
    def handle_Run_Button(self):
        # TO_DO
        # Split excel and append arrays to browser data
        
        print("Run Clicked")
        if self.ui.Comment_textEdit.toPlainText().strip() == "" :
            QtWidgets.QMessageBox.warning(self, "Warning", "Please Write a Comment before running.")
            return
        else:
            # Check Comment 
            print("Comment")
            print(self.ui.Comment_textEdit.toPlainText())
        
        # Check Message, If the user select sending a message , he must provide a message to send
        if self.ui.Message_textEdit.toPlainText().strip() == "" and self.ui.Message_checkBox.isChecked()== True:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please Write a Message before running.")
            return
        else:
            print("Message")
            print(self.ui.Message_textEdit.toPlainText())

        # Check if the file path is set
        if  self.file_path == None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file before running.")
            return
        
        
         # Check if the file is an Excel file
        if not (self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls')):
            QtWidgets.QMessageBox.warning(self, "Warning", "The selected file is not an Excel file. Please select a file of type .xlsx or .xls.")
            return
        
        # Here you can set the sheet name and number of splits
        sheet_name = "Sheet1"  # Replace with your actual sheet name
        # num_splits = 3  # self.num_of_accounts # Specify the number of splits # TO_DO # Change
        num_splits = self.num_of_accounts 

        if self.num_of_accounts > 0:
            try:
                # Call the split function
                arrays = split_excel_data(self.file_path, sheet_name, num_splits)
                print("Arrays")
                for i, array in enumerate(arrays):
                    # print(f"Arrays {i}: {array}")
                    # print(f"{i}")
                    self.browsers_data[i]['profile'] = array
                    print(f"self.browsers_data[{i}]")
                    print(self.browsers_data[i])
                    
                    # print(self.browsers_data[i][0])
                    # print(self.browsers_data[i][1])
                    # print(self.browsers_data[i][2])
                
                # For Debugging
                # print("self.browsers_data")
                # print(self.browsers_data)
                
                # Put the values of the comment, message, checkBox in variables to be passed tp contro_browser function
                comment_value_ui = self.ui.Comment_textEdit.toPlainText()
                message_value_ui = self.ui.Message_textEdit.toPlainText()
                IsMessageChecked_ui = self.ui.Message_checkBox.isChecked()

                # Create and start threads for each browser
                threads = []
                for data in self.browsers_data:
                    thread = threading.Thread(target=control_browser, args=(data['username'], data['password'], data['profile'], comment_value_ui, message_value_ui, IsMessageChecked_ui))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to complete
                for thread in threads:
                    thread.join()

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))
        else:
            # Show a warning message box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Enter at least one account first")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

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

def wait( type, x, y, element_no,driver): # TO_DO Check especially driver , can use the functionality directly without wait function
    global recover_flag
    # global driver
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

# Function to control a browser instance
def control_browser(username, password, profiles_array, comment_value, message_value, IsMessageChecked):
    # driver = myDRIVER
    driver = webdriver.Chrome()
    
    # Open Instagram's main page
    driver.get("https://www.instagram.com")

    # Optional: maximize the window
    # driver.maximize_window()

    # Wait for a few seconds to see the page
    time.sleep(15)
    
    # Example action: Entering a username (like on the Instagram login page)
    username_field = driver.find_element(By.NAME, "username")

    for letter in username:
        username_field.send_keys(letter)  # Send each letter
        time.sleep(0.1)  # Delay between letters

    # Wait for a few seconds before password
    time.sleep(3)

    password_field = driver.find_element(By.NAME, "password")
    for letter in password:
        password_field.send_keys(letter)  # Send each letter
        time.sleep(0.1)  # Delay between letters

    # Wait for a few seconds before password
    time.sleep(3)

    try:
        # Locate the Log In button using the provided XPath and click it
        login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()  # Click the Log In button

        # Wait for a few seconds 
        time.sleep(10)
    except:
        print("Can't Log In")
#######################################################################################################
#     # ## Debugging for one profile only 

#     # Navigate to client profile page
#     driver.get(f"https://www.instagram.com/{profiles_array[4][0]}/")
    
#     # Wait for the page to load and be visible (adjust the sleep time as necessary)
#     time.sleep(15)

#     try:
#         following_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Following')]") # Working
#         # following_button = driver.find_element(By.XPATH, "//div[text()='Following']") # Working
#         # following_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
#         print(f"Regarding user profile: {profiles_array[4][0]}") #TO_DO # Add thread number and more information
#         print("This user is already being followed.")

#     except:
#             # If the "Follow" button is not found, check for "Following"
#         try:
#             follow_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Follow')]") # Working
#             # follow_button = driver.find_element(By.XPATH, "//div[text()='Follow']") # Working
#             # follow_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
#             follow_button.click()  # Click to follow if "Follow" button is found
#             print(f"Regarding user profile: {profiles_array[4][0]}") #TO_DO # Add thread number and more information
#             print("Clicked 'Follow' button.")
#             # Wait for a few seconds
#             time.sleep(20)
        

#         except:
#             print("Neither 'Follow' nor 'Following' button found.")
# #######################################################################################################
#     try:
#         # Locate the Message button using the provided XPath and click it
#         message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working
#         # message_button = driver.find_element(By.XPATH, "//div[text()='Message']") # Working
#         # # message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']") # NOT Stable  
#         # # Click the "Message" button
#         message_button.click()
#         print("Clicked 'Message' button.")
#         # # Wait for a few seconds
#         time.sleep(10)

#     except:
#         print(" Error in 'Message' button.") # Print more information # TO_DO

#     try:
#         time.sleep(20)
#         # Locate POP Up Message using the provided XPath and click it
#         pop_up_message_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]") 
#         # pop_up_message_button = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
#         # # Click the "pop_up_message_button" button
#         pop_up_message_button.click()
#         print("Clicked Not Now in the pop up message")
#         # # Wait for a few seconds
#         time.sleep(10)

#     except:
#         try:
#             time.sleep(20)
#             # Locate POP Up Message using the provided XPath and click it
#             pop_up_message_button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Turn On')]") 
#             # pop_up_message_button2 = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
#             # # Click the "pop_up_message_button" button
#             pop_up_message_button2.click()
#             print("Clicked Not Now in the pop up message2")
#             # # Wait for a few seconds
#             time.sleep(10)

#         except:
#             print(" Error in Clicking pop up message2.") 

#     try:
#         time.sleep(20)
#         # Locate the Send Message Textbox using the provided XPath and click it
#         message_txtBox = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']") #Working # TO_DO # Improve 
#         # time.sleep(20)
       
#         # Click the "Message" button
#         # message_txtBox.click()
        
#         marketing_message1 = """Hello there! 🌹

# We hope you’re having a great day! ❤

# We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model! 📸

# Would you like to learn more about our ambassador program? 🎁🎁
# 📍| @petssparkle"""

#     #     marketing_message = (
#     #     "Hello there! "  
#     #     "We hope you’re having a great day! "  
#     #     "Would you like to learn more about our ambassador program? "
#     #     "| @petssparkle"  
#     # )
    
#     #     marketing_message2 = """Hello there!
#     #     We hope you’re having a great day!
#     #     We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
#     #     Would you like to learn more about our ambassador program? 
#     #     | @petssparkle"""

#         pyperclip.copy(marketing_message1)
#         time.sleep(10)
#         message_txtBox.click()  # Click to focus the text box
#         message_txtBox.send_keys(Keys.CONTROL, 'v')  # Paste the clipboard content
#         # Work around # TO_DO # Improve

#         # for letter in marketing_message2:
#         #     message_txtBox.send_keys(letter)  # Send each letter
#         #     time.sleep(0.2)  # Delay between letters

#         # Press the Enter key
#         message_txtBox.send_keys(Keys.RETURN)
#         time.sleep(5) 
#         print("Sending Message Successfully")

#     except:
#         print(" Error in Sending The Message") # Print more information # TO_DO
# #######################################################################################################  
#     driver.get(f"https://www.instagram.com/{profiles_array[4][0]}/")  #TO_DO #Like and commnt first? 
#     time.sleep(15)

#     try:
#         time.sleep(10)
#         # Locate the most recent Instagram post using the post grid
#         # Instagram posts are usually inside <a> tags with an <img> inside
#         # most_recent_post = driver.find_element(By.XPATH, "//article//img") 
#         most_recent_post = driver.find_element(By.XPATH, "//div[contains(@class, 'aagw')]") # Working # message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working

#         # Click on the most recent post
#         most_recent_post.click()

#         # Wait to see the post after clicking
#         time.sleep(5)  # Adjust time as needed for observation

#         print("Located post")

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     try:
#         time.sleep(10) 
#         current_url = driver.current_url
#         print("Current URL:", current_url)
#         time.sleep(5)
#         html = driver.page_source
#         soup = BeautifulSoup(html,features="html.parser")

#         LikeElement = wait("svg" ,"aria-label" , "Like" , 0,driver)

#         print(LikeElement)
#         likePAth = get_xpath(LikeElement)
#         print("original svg like path")
#         print(likePAth)
#         desired_Like_xpath = likePAth.rsplit("/", 3)[0]  
#         print("desired like path")
#         print(desired_Like_xpath)
#         time.sleep(5) 
#         likeButton = driver.find_element(By.XPATH, desired_Like_xpath)
#         print("Double Click")
#         time.sleep(5)
#         likeButton.click()
#         likeButton.click()
#         time.sleep(5)
#     except:
#         print("Error in Like Area")

    
#     try:
#         time.sleep(10)
#         time.sleep(5)
#         comment_area = driver.find_element(By.XPATH, "//textarea") 

#         # Click on the most recent post
#         # comment_area.click()
#         comment_area.send_keys("letter")  # Send each letter

#         # Wait to see the post after clicking
#         time.sleep(5)  # Adjust time as needed for observation

#         print("Located Comment 2")

#     except Exception as e:
#         print("An error occurred in Comment way 2 ")
#         try:
#             time.sleep(15)
#             # Locate the most recent Instagram post using the post grid
#             # Instagram posts are usually inside <a> tags with an <img> inside
#             # most_recent_post = driver.find_element(By.XPATH, "//article//img") 
#             comment_area = driver.find_element(By.XPATH, "//textarea[contains(@class, 'xvbhtw8 ')]") # Working # MORE STABLE
#             comment_message = """ Check your DMs, Please  🌹 """
#             pyperclip.copy(comment_message)
#             time.sleep(5)
#             # Click on the most recent post
#             # comment_area.send_keys("letter")
#             comment_area.send_keys(Keys.CONTROL, 'v')
#             time.sleep(1)
#             comment_area.send_keys(Keys.RETURN)
#             # Wait to see the post after clicking
#             time.sleep(5)  # Adjust time as needed for observation

#             print(" Located Comment By Way 3")

#         except Exception as e:
#             # print(f"An error occurred: {e}")
#             print("An error occurred in Comment way 3 ")
#             try:
#                 CommentElement = wait("textarea" ,"aria-label" , "Add a comment..." , 0,driver)

#                 # print(CommentElement)
#                 CommentPath = get_xpath(CommentElement)
#                 comment_area = driver.find_element(By.XPATH, CommentPath)
#                 comment_message = """ Check your DMs, Please  🌹 """
#                 pyperclip.copy(comment_message)
#                 time.sleep(5)
#                 # Click on the most recent post
#                 # comment_area.send_keys("letter")
#                 comment_area.send_keys(Keys.CONTROL, 'v')
#                 time.sleep(1)
#                 comment_area.send_keys(Keys.RETURN)

#                 # Wait to see the post after clicking
#                 time.sleep(5)  # Adjust time as needed for observation
#                 print(" Located Comment By Soup Way1")
#             except:    
#                 print("An error occurred in Comment way 1 ")
#######################################################################################################
    # Wait for a few seconds
    time.sleep(10)
    for i in range(len(profiles_array)):
        try:
            # Navigate to client profile page
            driver.get(f"https://www.instagram.com/{profiles_array[i][0]}/")
            # Wait for the page to load and be visible (adjust the sleep time as necessary)
            time.sleep(15)
            print(f"Success: Customer Profile Page {profiles_array[i][0]}, From Account {username}")
        except:
            print(f"Failed: Can't get Customer Profile Page {profiles_array[i][0]}, From Account {username}")

        try:
            following_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Following')]") # Working
            # following_button = driver.find_element(By.XPATH, "//div[text()='Following']") # Working
            # following_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
            print(f"Regarding user profile: {profiles_array[i][0]}, From Account {username} ") #TO_DO # Add thread number and more information
            print("This user is already being followed.")

        except:
            # If the "Follow" button is not found, check for "Following"
            try:
                follow_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Follow')]") # Working
                # follow_button = driver.find_element(By.XPATH, "//div[text()='Follow']") # Working
                # follow_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
                follow_button.click()  # Click to follow if "Follow" button is found
                print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                print("Clicked 'Follow' button.")
                # Wait for a few seconds
                time.sleep(10)
        

            except:
                print("Neither 'Follow' nor 'Following' button found.")

        # If User Want to send a Message
        if IsMessageChecked == True:
            try:
                # Locate the Message button using the provided XPath and click it
                message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working
                # message_button = driver.find_element(By.XPATH, "//div[text()='Message']") # Working
                # # message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']") # NOT Stable  
                # # Click the "Message" button
                message_button.click()
                print("Clicked 'Message' button.")
                # # Wait for a few seconds
                time.sleep(5)

            except:
                print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                print(" Error in 'Message' button.") # Print more information # TO_DO
        

        
            try:
                time.sleep(20)
                # Locate POP Up Message using the provided XPath and click it
                pop_up_message_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]") 
                # pop_up_message_button = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
                # # Click the "pop_up_message_button" button
                pop_up_message_button.click()
                print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                print("Clicked Not Now in the pop up message")
                # # Wait for a few seconds
                time.sleep(10)

            except:
                try:
                    time.sleep(20)
                    # Locate POP Up Message using the provided XPath and click it
                    pop_up_message_button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Turn On')]") 
                    # pop_up_message_button2 = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
                    # # Click the "pop_up_message_button" button
                    pop_up_message_button2.click()
                    print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                    print("Clicked Not Now in the pop up message2")
                    # # Wait for a few seconds
                    time.sleep(10)

                except:
                    print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                    print(" Error in Clicking pop up message2.") 

            try:
                time.sleep(10)        
                # Locate the Send Message Textbox using the provided XPath and click it
                message_txtBox = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']") #Working # TO_DO # Improve 
                # time.sleep(20)       
                # # Click the "Message" button
                # message_txtBox.click()
                marketing_message1 = message_value
    #             marketing_message1 = """Hello there! 🌹
    
    # We hope you’re having a great day! ❤

    # We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model! 📸

    # If you are interested, Kindly send "Pets Sparkle Star" in a message to our official page! 🎁🎁
    # 📍| @petssparkle_official"""

                # marketing_message = """Hello there!
                # We hope you’re having a great day!
                # We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
                # Would you like to learn more about our ambassador program?
                # | @petssparkle"""
        
                pyperclip.copy(marketing_message1)
                time.sleep(5)
                message_txtBox.click()  # Click to focus the text box
                message_txtBox.send_keys(Keys.CONTROL, 'v')  # Paste the clipboard content 
                time.sleep(5)
            
                # for letter in marketing_message:
                #     message_txtBox.send_keys(letter)  # Send each letter
                #     time.sleep(0.2)  # Delay between letters

                # Press the Enter key
                message_txtBox.send_keys(Keys.RETURN)
                time.sleep(5)
                print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                print("Sending Message Successfully") # Print more information # TO_DO
            

            except:
                print(f"Regarding user profile: {profiles_array[i][0]} , From Account {username}") #TO_DO # Add thread number and more information
                print(" Error in Sending The Message") # Print more information # TO_DO
 
            try:
                # Navigate to client profile page
                driver.get(f"https://www.instagram.com/{profiles_array[i][0]}/")
                # Wait for the page to load and be visible (adjust the sleep time as necessary)
                time.sleep(15)
                print(f"Success: Customer Profile Page {profiles_array[i][0]}, From Account {username}")
            except:
                print(f"Failed: Can't get Customer Profile Page {profiles_array[i][0]}, From Account {username}")
            time.sleep(15)
########################################################################################################## 
        try:
            time.sleep(10)
            # Locate the most recent Instagram post using the post grid
            # Instagram posts are usually inside <a> tags with an <img> inside
            # most_recent_post = driver.find_element(By.XPATH, "//article//img") 
            most_recent_post = driver.find_element(By.XPATH, "//div[contains(@class, 'aagw')]") # Working # message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working

            # Click on the most recent post
            most_recent_post.click()

            # Wait to see the post after clicking
            time.sleep(5)  # Adjust time as needed for observation

            print("Located post")

        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            time.sleep(10) 
            current_url = driver.current_url
            print("Current URL:", current_url)
            time.sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html,features="html.parser")

            LikeElement = wait("svg" ,"aria-label" , "Like" , 0,driver)

            print(LikeElement)
            likePAth = get_xpath(LikeElement)
            print("original svg like path")
            print(likePAth)
            desired_Like_xpath = likePAth.rsplit("/", 3)[0]  
            print("desired like path")
            print(desired_Like_xpath)
            time.sleep(5) 
            likeButton = driver.find_element(By.XPATH, desired_Like_xpath)
            print("Double Click")
            time.sleep(5)
            likeButton.click()
            likeButton.click()
            time.sleep(5)
        except:
            print("Error in Like Area")

    
        try:
            time.sleep(10)
            time.sleep(5)
            comment_area = driver.find_element(By.XPATH, "//textarea") 

            # Click on the most recent post
            # comment_area.click()
            comment_message = comment_value
            # comment_message = """ Check your DMs, Please  🌹 """
            pyperclip.copy(comment_message)
            time.sleep(5)
            # Click on the most recent post
            # comment_area.send_keys("letter")
            comment_area.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            comment_area.send_keys(Keys.RETURN)

            # Wait to see the post after clicking
            time.sleep(5)  # Adjust time as needed for observation

            print("Located Comment 2")

        except Exception as e:
            print("An error occurred in Comment way 2 ")
            try:
                time.sleep(15)
                # Locate the most recent Instagram post using the post grid
                # Instagram posts are usually inside <a> tags with an <img> inside
                # most_recent_post = driver.find_element(By.XPATH, "//article//img") 
                comment_area = driver.find_element(By.XPATH, "//textarea[contains(@class, 'xvbhtw8 ')]") # Working # MORE STABLE
                comment_message = """ Check your DMs, Please  🌹 """
                pyperclip.copy(comment_message)
                time.sleep(5)
                # Click on the most recent post
                # comment_area.send_keys("letter")
                comment_area.send_keys(Keys.CONTROL, 'v')
                time.sleep(1)
                comment_area.send_keys(Keys.RETURN)
                # Wait to see the post after clicking
                time.sleep(5)  # Adjust time as needed for observation

                print(" Located Comment By Way 3")

            except Exception as e:
                # print(f"An error occurred: {e}")
                print("An error occurred in Comment way 3 ")
                try:
                    CommentElement = wait("textarea" ,"aria-label" , "Add a comment..." , 0,driver)

                    # print(CommentElement)
                    CommentPath = get_xpath(CommentElement)
                    comment_area = driver.find_element(By.XPATH, CommentPath)
                    comment_message = """ Check your DMs, Please  🌹 """
                    pyperclip.copy(comment_message)
                    time.sleep(5)
                    # Click on the most recent post
                    # comment_area.send_keys("letter")
                    comment_area.send_keys(Keys.CONTROL, 'v')
                    time.sleep(1)
                    comment_area.send_keys(Keys.RETURN)

                    # Wait to see the post after clicking
                    time.sleep(5)  # Adjust time as needed for observation
                    print(" Located Comment By Soup Way1")
                except:    
                    print("An error occurred in Comment way 1 ")
##########################################################################################################

##########################################################################################################
##########################################################################################################
    # Keep the browser open for observation
    input("Press Enter to close this browser...") # TO_DO Try to close thread or take useful input from user
    
    driver.quit()


def split_excel_data(file_path, sheet_name, num_splits):
    """
    Splits the data from an Excel sheet into a specified number of arrays.

    Parameters:
    - file_path: Path to the Excel file.
    - sheet_name: Name of the sheet to read.
    - num_splits: The number of arrays to split the data into.

    Returns:
    - A list of arrays, each containing a portion of the original data.
    """
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Convert the DataFrame to a list (array)
    data_array = df.values.tolist()  # This converts the DataFrame to a list of lists
    
    # Determine the length of the data
    length = len(data_array)

    # Check if the requested number of splits is valid
    if num_splits <= 0:
        raise ValueError("Number of splits must be greater than 0.")
    
    # If we have fewer rows than splits, return the entire data array as a single array
    if length < num_splits:
        return [data_array]  # Return the whole data as one array

    # Calculate the split size
    split_size = length // num_splits
    
    # Create a list to hold the split arrays
    split_arrays = []
    
    for i in range(num_splits):
        if i == num_splits - 1:  # Last array takes any remaining data
            split_arrays.append(data_array[i * split_size:])  # Remaining part
        else:
            split_arrays.append(data_array[i * split_size:(i + 1) * split_size])  # Regular split

    return split_arrays

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())