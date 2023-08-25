"""
This program is used to learn the basics of creating a GUI window with PyQT5 using only the Python code and not
the drag and drop option. 
 """

# All import statements
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    # Create an instance of the application and the Window
    app = QApplication([])
    window = QWidget()
    window.setGeometry(250, 250, 1000, 500) #set the size and placement of the window
    window.setWindowTitle("My First QT Window!") #set the label of the window

    # Create the layout of the window (verticle)
    layout = QVBoxLayout()

    buttonLabel = QLabel("Do you dare press the button?")
    textbox = QTextEdit()
    button = QPushButton("Press me!!!")

    # Connect a function to the button using lambda
    button.clicked.connect(lambda: button_click(textbox.toPlainText()))


    layout.addWidget(buttonLabel)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()


def button_click(msg):
    """
    The purpose of this method is to define what happens when the button is clicked. In this
    particular case a message box appears on screen.
    """
    message = QMessageBox()
    message.setText("You crazy motha fuka!!!\n" + msg)
    message.exec_()


# A call to the main function
if __name__ == '__main__':
    main()