from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Create the application instance
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Hello World")
window.setGeometry(300, 300, 300, 300)

# Create a vertical layout for the main window
layout = QVBoxLayout()

# Add a label to the layout
label = QLabel("Enter your name:")
layout.addWidget(label)

# Add a line edit widget to the layout for entering the name
lineEdit = QLineEdit()
layout.addWidget(lineEdit)

# Add a button to the layout
button = QPushButton("Click me")
layout.addWidget(button)

# Set the layout for the main window
window.setLayout(layout)

# Show the main window
window.show()


# Define a function to handle button click events
@pyqtSlot()
def clicked():
    # Retrieve the name entered in the line edit widget
    name = lineEdit.text()

    # Create a message box
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Hello, " + name)  # Display the greeting message with the entered name
    msg.setWindowTitle("Hello")  # Set the title of the message box

    # Show the message box
    msg.exec_()


# Connect the clicked signal of the button to the clicked function
button.clicked.connect(clicked)

# Start the event loop
app.exec_()
