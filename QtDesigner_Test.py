"""
This program is an was used to learn about using Qt Designer. The GUI contains a username and password text field and 
a login button. If the input is correct then a large text box and another button are enabled. If you enter text and click
the new button then the message is transfered to a pop op box. 

Required File: DesignerTestGUI.ui
"""

# Import to use qtwidgets ( uic is needed to import the .ui file)
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    # Constructor used to create the window based on the .ui file
    def __init__(self):
        super(MyGUI, self).__init__()

        # Load the ui file
        uic.loadUi("DesignerTestGUI.ui", self)
        self.show()

        # Connect the login button funct
        self.login_button.clicked.connect(self.login)
        # Connect the do something button
        self.do_button.clicked.connect(lambda: self.do_something(self.large_text.toPlainText()))
        # Exit program if close is selected from the drop down
        self.actionClose.triggered.connect(exit)


    def login(self):
        """
        This method is used to check the login and password when the login button is clicked.
        If the incorrect info is input then an error message is displayed.
        """
        if self.username_ledit.text() == "username" and self.pass_ledit.text() == "password":
            self.large_text.setEnabled(True)
            self.do_button.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()


    def do_something(self, msg):
        """
        This method is used then the do something button is clicked. The button is only active
        after the correct username and password have been input. The do something button will
        transfer the text to a pop up box.
        """
        message = QMessageBox()
        message.setText(msg)
        message.exec_()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()