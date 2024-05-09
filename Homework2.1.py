import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

# Initialize an empty list to store scores
score_list = []


# Function to convert score to grade
def convert_score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# Function to update score status
def update_score_status():
    try:
        score = int(score_entry.text())
        if score > 100 or score < 0:
            QMessageBox.critical(window, "Error", "The score should be between 0 and 100.")
        else:
            grade = convert_score_to_grade(score)
            score_list.append(score)
            sum_scores = sum(score_list)
            count = len(score_list)
            avg = sum_scores / count
            status_label.setText(f"Grade: {grade} | Count: {count} | Sum: {sum_scores} | Average: {avg:.2f}")

            # Update histogram
            histogram_canvas.clear()
            histogram_canvas.hist(score_list, bins=10, edgecolor='black')
            histogram_canvas.set_xlabel('Score Range')
            histogram_canvas.set_ylabel('Frequency')
            histogram_canvas.set_title('Score Distribution in the Class')
            histogram_canvas.grid(True)
            histogram_canvas.figure.canvas.draw()

            # Clear text box
            score_entry.clear()

    except ValueError:
        QMessageBox.critical(window, "Error", "Please enter a valid integer score.")


# Function to handle Enter key press
def handle_enter():
    update_score_status()


# Function to close the application
def close_application():
    app.quit()


# Create the main application window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Score Tracker")

# Create widgets
score_label = QLabel("Enter Score:")
score_entry = QLineEdit()
update_button = QPushButton("Update")
exit_button = QPushButton("Exit")
status_label = QLabel("Score status will be displayed here")

# Create layout
layout = QVBoxLayout()
layout.addWidget(score_label)
layout.addWidget(score_entry)
layout.addWidget(update_button)
layout.addWidget(exit_button)
layout.addWidget(status_label)

# Create a canvas for plotting histogram
histogram_canvas = plt.figure()
histogram_canvas = histogram_canvas.add_subplot(111)
histogram_canvas.grid(True)
histogram_canvas_canvas = FigureCanvas(histogram_canvas.figure)
layout.addWidget(histogram_canvas_canvas)

# Connect button click event to update_score_status function
update_button.clicked.connect(update_score_status)
exit_button.clicked.connect(close_application)

# Allow updating using Enter key
score_entry.returnPressed.connect(handle_enter)

# Set layout
window.setLayout(layout)
window.show()

# Run the application
sys.exit(app.exec_())