import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import threading
import time

# Define the scope
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# JSON credentials as a string (replace with your actual JSON content)
json_credentials = """{
  "type": "service_account",
  "project_id": "instgram-bot-credentials",
  "private_key_id": "e2433097e3d8730a83f37b753b87ec1fdc4837ab",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCRgc/nqtpnK8fZ\\n7Br4IkymLGfGB4oTxK4OETWADF8dwjQg5DctMjUygXO6hh2RNskTto5Pki2Qgecs\\nISxdQXciUxyEXsBgYkDcXiSZqckwMcKqcIYTCoCNJ504HA8mFpSXNcGGH390LbUv\\nAGQgElOhcgbSqeTMeg7UPif9Iqui1HTF3it0rH9uDlAh3/5yMxqDRzGRcS+Oqo9x\\nOq0quw7hukg6YHrc94OPZmuaCskf2ptYlulVUnoEGvJRaIpQcG9iwcIQyi4toFhX\\nrSLLaBeR4WUU3BDM1ZcGKSNsRz3yKrR5SaGW4K0yqcg4Ut7OJGAoc2GzXj9ZihYD\\nhjZ3E/o5AgMBAAECggEAF3Kkzz9gHJoYhYyft/bHBUxImMfkP1VFeyzYwz67IS+H\\nePltztG1cuMbhCZSo3EBrDSR8E6tGwlj+F+MJ6cCDLz57nbaZ23N5/UfzsdmjWan\\naRHi+TSLDLQiiMU0x72BynA2NGflARLQjLdyaxyo725RnScVoMHWm+s8RHWO1RlL\\nT2PBcx2Dd6x0KxpBpdsCu60nbaFkz/KYOwqNk9ib4M/dXG0JH8oWtDXrWUn0lSm9\\nxwb5s0WBI5nIme5HYSGAxOjcxp78IEM7UZnYxF4B2XSpWrqKXjk9gyL/NTwtLOL8\\npvEfqwd7hxmsYUsf3vz/IO3vmPIelxFtX11nBXnrJQKBgQDHZuo33zZRJJ3fucbr\\nrEGdM/YiCBwfxoVCVt2fZLJedvbFrF665XMt4bYb/UYAGzwAfHTRT7SNHQhN0RTN\\ntYwEhfv1eKQSKPeL79ual190U3iXoswh3Dl+YeV41vxhPFHCWhhzsGjKQdJjw+Wk\\nzMp5A/dp4L91c4eYWVE8EpeMowKBgQC6zr8vRCMMGo+LAkE+ymM1vH82G5PIzGbw\\nauT6OfIaoIjYPIzmLG2PrYc13UOpQrcEI/A9Dgwo2I4LT4Koec6tLGLbzi+X7YBa\\nEaQMc8Q6Df1NWevvNlV3iFoB4/dxIZEPjRP6ucQPST2BIbUFmGs7VI0FNMaBV919\\nYQgNQRjPcwKBgC5XdbGcd6QuDV7Uby2QcANX8yj/l4GvAoNjashDf8zCeyF/qNho\\nwPb10Pv6Rc16htxaEFAg5QYyrB5hrCMOwUa/2Mm4yvDJgpaMHQ51haKkT492L1jj\\nNJ1xpQILfMYgXaP8ilhAtGnlGD9FZNaDHb84M8Twja5/NhErGN0MORpfAoGAMLPC\\nCFKdSISMM9OMqxAcuV/BUpvx9YHEvJ1BwTLmOabsxmNS4JdooPK+s35SK4inKj8s\\nXN6SsPt0XOKHz+Chz2gpBeFFaziSI+lBebWczP3ksgvlhOIHejhkLuX+FtKHfSRs\\ntwtDYDDaBhaBmUnZewhaE6dksUf1CMEJVltIWp0CgYEAijXUq1p1hbGlV1kX8USY\\nQ0whZLP8ru5OBLaHk1HlwcwJ9U1de2dHDPR2D9swRXhRTzG0/xngOHFLnz6phEfL\\nKQlQN/+mXtS9KSctQJtPYRFH+w60a44FnW2B8Q9TukF6Qcwtp0a14X5LzeL+x5gS\\nG9wcWTxc/VOkx0gxVomOAjI=\\n-----END PRIVATE KEY-----\\n",
  "client_email": "insta-bot-account@instgram-bot-credentials.iam.gserviceaccount.com",
  "client_id": "102217871465761600519",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/insta-bot-account%40instgram-bot-credentials.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}"""

# Load the credentials from the string
credentials_dict = json.loads(json_credentials)
# Create a credentials object
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
# Authorize the client
client = gspread.authorize(creds)

# # Load the credentials from the JSON key file
# creds = ServiceAccountCredentials.from_json_keyfile_name("instgram-bot-credentials-e2433097e3d8.json", scope)

# Now you can access your Google Sheet
spreadsheet = client.open('Instgram_Bot')  # Replace with your actual sheet title
worksheet = spreadsheet.sheet1  # You can also use get_worksheet(index)

# # Read data from a specific cell
# value = worksheet.acell('B2').value   # Replace 'A1' with the desired cell reference
# print(f"The value in cell B2 is: {value}")

# # Example: Reading all values in a column
# column_values = worksheet.col_values(1)  # Gets all values in the first column
# print(column_values)

# # Function to check the value of cell B2
# def check_b2_value():
#     while True:
#         value = worksheet.acell('B2').value
#         print(f"Current value in B2: {value}")
#         if value != '1':
#             print("Value in B2 is not 1. Terminating all threads.")
#             terminate_threads()
#             break
#         time.sleep(300)  # Wait for 5 minutes

# # Function to terminate all threads
# def terminate_threads():
#     # You could set a flag or use other means to stop your threads
#     print("All operations terminated.")

# # Start the checking thread
# check_thread = threading.Thread(target=check_b2_value)
# check_thread.start()

# # Here you can add other thread functions or operations that will run concurrently
# # For example:
# def other_operations():
#     while True:
#         # Simulate some operations
#         print("Running other operations...")
#         time.sleep(10)  # Simulate work being done

# # Start other operations in a separate thread
# operations_thread = threading.Thread(target=other_operations)
# operations_thread.start()
# Create a threading event for termination
terminate_event = threading.Event()

# Function to check the value of cell B2 every 5 minutes
def check_b2_value():
    while True:
        value = worksheet.acell('B2').value
        print(f"Current value in B2: {value}")
        if value == '0':  # Check if B2 is zero
            print("Value in B2 is zero. Terminating all threads.")
            terminate_event.set()  # Signal all threads to terminate
            break
        time.sleep(300)  # Wait for 5 minutes

# Function to perform some operations
def perform_operations(thread_id):
    while not terminate_event.is_set():
        # Simulate some operations
        print(f"Thread {thread_id} is running...")
        time.sleep(10)  # Simulate work being done
    print(f"Thread {thread_id} is terminating.")

# Start the checking thread
check_thread = threading.Thread(target=check_b2_value)
check_thread.start()

# Start multiple operation threads
num_threads = 5  # Number of parallel threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=perform_operations, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for the checking thread to finish
check_thread.join()

# Wait for all operation threads to finish
for thread in threads:
    thread.join()

print("All threads have been terminated.")