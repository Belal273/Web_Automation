# backend.py
import sys
from PyQt5 import QtWidgets
from frontend_Basic import Ui_MainWindow  # Import the frontend UI class

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Additional logic can go here
        self.setup_connections()
        self.ui.Run_pushButton.clicked.connect(self.handle_Run_Buttonr)

    def setup_connections(self):
        # Example: Connecting signals to slots
        self.ui.Browse_pushButton.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        # Logic for what happens when the button is clicked
        print("Button clicked in backend!")
    
    def handle_Run_Buttonr(self):
        print("Run Clicked")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())