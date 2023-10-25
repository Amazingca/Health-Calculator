
import qdarkstyle
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QGridLayout

class CheckInWindow(QMainWindow):
    def __init__(self, profile_name, today_date):
        super().__init__()

         # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health Calculator Demo")
        self.setFixedSize(QSize(294, 150))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set Up Layout of Window 
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Set Up Header 
        self.header = QLabel("<b>Check in for " + profile_name + " on " + today_date + "<b>") 
        self.layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Set up Info Fields and Labels 
        self.info_layout = QGridLayout()
        self.current_weight_label = QLabel("Current Weight (lb)")
        self.current_weight = QPlainTextEdit()
        self.current_weight.setMinimumHeight(30) 
        self.current_weight.setMaximumHeight(30)
        self.info_layout.addWidget(self.current_weight_label, 0, 0)
        self.info_layout.addWidget(self.current_weight, 0, 1)
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.info_layout)

        # Set Up Buttons
        self.button_layout = QGridLayout()
        self.update_button = QPushButton("Check In")
        self.cancel_button = QPushButton("Cancel")
        self.button_layout.addWidget(self.update_button, 0, 0)
        self.button_layout.addWidget(self.cancel_button, 0, 1)
        self.layout.addLayout(self.button_layout)


