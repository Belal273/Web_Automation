# backend.py
import sys
import pandas as pd
from PyQt5 import QtWidgets
from frontend_Adv import Ui_MainWindow  # Import the frontend UI class
from PyQt5.QtWidgets import QMessageBox


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