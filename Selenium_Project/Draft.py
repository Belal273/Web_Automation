# Original XPath
original_xpath = "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div/div/span/svg"

# Desired XPath
# Remove the last part: "/div/span/svg"
desired_xpath = original_xpath.rsplit("/", 3)[0]  

# Print the result
print("Original XPath:", original_xpath)
print("Desired XPath:", desired_xpath)