# backend.py
import sys
import pandas as pd
from PyQt5 import QtWidgets
from frontend_Basic import Ui_MainWindow  # Import the frontend UI class

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Initialize file path
        self.file_path = None  # Initialize the file_path attribute

        # Additional logic can go here
        self.setup_connections()
        self.ui.Run_pushButton.clicked.connect(self.handle_Run_Buttonr)

    def setup_connections(self):
        # Example: Connecting signals to slots
        self.ui.Browse_pushButton.clicked.connect(self.handle_browse_button_click)

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
    
    def handle_Run_Buttonr(self):
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
        num_splits = 3  # Specify the number of splits

        try:
            # Call the split function
            arrays = split_excel_data(self.file_path, sheet_name, num_splits)
            print("Arrays")
            for i, array in enumerate(arrays):
                print(f"Arrays {i}: {array}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

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