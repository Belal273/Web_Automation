import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading
import pandas as pd

# Function to control a browser instance
def control_browser(username, password, profiles_array):
    driver = webdriver.Chrome()
    # Open Instagram's main page
    driver.get("https://www.instagram.com")

    # Optional: maximize the window
    driver.maximize_window()
    # Wait for a few seconds to see the page
    time.sleep(5)
    # Optional: maximize the window
    # driver.maximize_window()
    # Wait for a few seconds to see the page
    time.sleep(10)
    
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

        # Keep the browser open
        # input("Press Enter to go to client profile page ")  # Wait for user input
        # Wait for a few seconds 
        time.sleep(10)
    except:
        print("Can't Log In")
#######################################################################################################
    # ## Debugging for one profile only 

    # # Navigate to client profile page
    # driver.get(f"https://www.instagram.com/{profiles_array[6][0]}/")
    
    # # Wait for the page to load and be visible (adjust the sleep time as necessary)
    # time.sleep(20)

    # try:
    #     following_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Following')]") # Working
    #     # following_button = driver.find_element(By.XPATH, "//div[text()='Following']") # Working
    #     # following_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
    #     print(f"Regarding user profile: {profiles_array[0][0]}") #TO_DO # Add thread number and more information
    #     print("This user is already being followed.")

    # except:
    #         # If the "Follow" button is not found, check for "Following"
    #     try:
    #         follow_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Follow')]") # Working
    #         # follow_button = driver.find_element(By.XPATH, "//div[text()='Follow']") # Working
    #         # follow_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']") # NOT Stable  
    #         follow_button.click()  # Click to follow if "Follow" button is found
    #         print(f"Regarding user profile: {profiles_array[0][0]}") #TO_DO # Add thread number and more information
    #         print("Clicked 'Follow' button.")
    #         # Wait for a few seconds
    #         time.sleep(20)
        

    #     except:
    #         print("Neither 'Follow' nor 'Following' button found.")

    
    # try:
    #     # Locate the Message button using the provided XPath and click it
    #     message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Message')]") # Working
    #     # message_button = driver.find_element(By.XPATH, "//div[text()='Message']") # Working
    #     # # message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']") # NOT Stable  
    #     # # Click the "Message" button
    #     message_button.click()
    #     print("Clicked 'Message' button.")
    #     # # Wait for a few seconds
    #     time.sleep(10)

    # except:
    #     print(" Error in 'Message' button.") # Print more information # TO_DO

    # try:
    #     time.sleep(20)
    #     # Locate POP Up Message using the provided XPath and click it
    #     pop_up_message_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]") 
    #     # pop_up_message_button = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
    #     # # Click the "pop_up_message_button" button
    #     pop_up_message_button.click()
    #     print("Clicked Not Now in the pop up message")
    #     # # Wait for a few seconds
    #     time.sleep(10)

    # except:
    #     try:
    #         time.sleep(20)
    #         # Locate POP Up Message using the provided XPath and click it
    #         pop_up_message_button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Turn On')]") 
    #         # pop_up_message_button2 = driver.find_element(By.XPATH, "//button[text()='Not Now']") 
    
    #         # # Click the "pop_up_message_button" button
    #         pop_up_message_button2.click()
    #         print("Clicked Not Now in the pop up message2")
    #         # # Wait for a few seconds
    #         time.sleep(10)

    #     except:
    #         print(" Error in Clicking pop up message2.") 


    
    
    
    
    # try:
    #     time.sleep(20)
    #     # Locate the Send Message Textbox using the provided XPath and click it
    #     message_txtBox = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']") #Working # TO_DO # Improve 
    #     # time.sleep(20)
       
    #     # Click the "Message" button
    #     # message_txtBox.click()
        
    #     marketing_message1 = """Hello there! 🌹

    #     We hope you’re having a great day! ❤

    #     We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model! 📸

    #     Would you like to learn more about our ambassador program? 🎁🎁
    #     📍| @petssparkle"""

    #     marketing_message = (
    #     "Hello there! "  
    #     "We hope you’re having a great day! "  
    #     "Would you like to learn more about our ambassador program? "
    #     "| @petssparkle"  
    # )
    
    #     marketing_message2 = """Hello there!
    #     We hope you’re having a great day!
    #     We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
    #     Would you like to learn more about our ambassador program? 
    #     | @petssparkle"""

    #     pyperclip.copy(marketing_message1)
    #     time.sleep(10)
    #     message_txtBox.click()  # Click to focus the text box
    #     message_txtBox.send_keys(Keys.CONTROL, 'v')  # Paste the clipboard content
    #     # Work around # TO_DO # Improve

    #     # for letter in marketing_message2:
    #     #     message_txtBox.send_keys(letter)  # Send each letter
    #     #     time.sleep(0.2)  # Delay between letters

    #     # Press the Enter key
    #     message_txtBox.send_keys(Keys.RETURN)

    # except:
    #     print(" Error in Sending The Message") # Print more information # TO_DO

#######################################################################################################
    # Wait for a few seconds
    time.sleep(20)
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
            marketing_message1 = """Hello there! 🌹

We hope you’re having a great day! ❤

We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model! 📸

If you are interested, Kindly send "Pets Sparkle Star" in a message to our official page! 🎁🎁
📍| @petssparkle_official"""

            marketing_message = """Hello there!
            We hope you’re having a great day!
            We’re the petssparkle marketing team, and we really like your profile. It looks like you could be our next spotlight model!
            Would you like to learn more about our ambassador program?
            | @petssparkle"""
        
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
##########################################################################################################
    # Keep the browser open for observation
    input("Press Enter to close this browser...")
    
    driver.quit()




def split_excel_data(file_path, sheet_name):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Convert the DataFrame to a list (array)
    data_array = df.values.tolist()  # This converts the DataFrame to a list of lists
    
    # Determine the split size
    split_size = len(data_array) // 4
    
    # Split the data array into 4 separate arrays
    array1 = data_array[:split_size]               # First quarter
    array2 = data_array[split_size:2 * split_size] # Second quarter
    array3 = data_array[2 * split_size:3 * split_size] # Third quarter
    array4 = data_array[3 * split_size:]           # Fourth quarter
    
    return array1, array2, array3, array4


def split_excel_data_to_3 (file_path, sheet_name):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Convert the DataFrame to a list (array)
    data_array = df.values.tolist()  # This converts the DataFrame to a list of lists
    
    # Determine the split size
    length = len(data_array)
    split_size = length // 3
    
    # Split the data array into 3 separate arrays
    array1 = data_array[:split_size]                # First part
    array2 = data_array[split_size:2 * split_size]  # Second part
    array3 = data_array[2 * split_size:]            # Remaining part
    
    return array1, array2, array3

# Example usage
# file_path = 'instagram (7).xlsx'  # Replace with your Excel file path
# sheet_name = 'instagram (7)'  # Replace with your sheet name if different
file_path = 'instagram.xlsx'  # Replace with your Excel file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different

# arrays = split_excel_data(file_path, sheet_name) #TO_DO # Check n Change
arrays = split_excel_data_to_3 (file_path, sheet_name) #TO_DO # Check n Change

# # Print the resulting arrays
# for i, array in enumerate(arrays, start=1):
#     print(f"\nArray {i}:")
#     print(array)
# Print the resulting arrays
# for array in arrays:
#     print(f"\nArray :")
#     print(array)

# List of URLs and usernames to automate
browsers_data = [
# { 'username': 'petssparkle.009', 'password': 'petssparkle&1', 'profile': arrays[0]}, # Panned
{ 'username': 'petssparkle.06', 'password': 'petssparkle&12', 'profile': arrays[0]}, # No Message Sent
# { 'username': 'petssparkle.09', 'password': 'petssparkle&12', 'profile': arrays[1]}, # Sent one message 
{ 'username': 'petssparkle.u11', 'password': 'petssparkle&11', 'profile': arrays[1]} # No Message Sent
]

# Create and start threads for each browser
threads = []
for data in browsers_data:
    thread = threading.Thread(target=control_browser, args=(data['username'], data['password'], data['profile']))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()


##########################################################################################################
# DRAFT
# Testing the thread Idea
# import threading

# def print_numbers():
#     for i in range(10):
#         print(i)

# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_numbers)

# # Starting threads
# thread1.start()
# thread2.start()

# # Joining threads to wait for them to finish
# thread1.join()
# thread2.join()
