import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Load the credentials from the JSON key file
creds = ServiceAccountCredentials.from_json_keyfile_name("instgram-bot-credentials-e2433097e3d8.json", scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by its title or key
spreadsheet = client.open('Instgram_Bot')  # Replace with your actual sheet title
worksheet = spreadsheet.sheet1  # You can also use get_worksheet(index)

# Read data from a specific cell
value = worksheet.acell('A1').value   # Replace 'A1' with the desired cell reference
print(f"The value in cell A1 is: {value}")

# Example: Reading all values in a column
column_values = worksheet.col_values(1)  # Gets all values in the first column
print(column_values)