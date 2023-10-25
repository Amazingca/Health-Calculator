

import qdarkstyle
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QGridLayout


class UpdateInfoWindow(QMainWindow):
    def __init__(self, profile_name):
        super().__init__()

         # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health Calculator Demo")
        self.setFixedSize(QSize(400, 300))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set Up Layout of Window 
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Set Up Header 
        self.header = QLabel("<b>Update Profile: " + profile_name + "<b>") 
        self.layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Set up Info Fields and Labels 
        self.profile_name_label = QLabel("Name")
        self.profile_name = QPlainTextEdit()
        self.current_weight_label = QLabel("Current Weight (lb)")
        self.current_weight = QPlainTextEdit()
        self.goal_weight_label = QLabel("Goal Weight (lb)")
        self.goal_weight = QPlainTextEdit()
        self.age_label = QLabel("Age")
        self.age = QPlainTextEdit()
        self.activity_level_label = QLabel("Activity Level (0-4)")
        self.activity_level = QPlainTextEdit()
        self.height_label = QLabel("Height (in)")
        self.height_ = QPlainTextEdit()
        self.gender_label = QLabel("Gender (m/f)")
        self.gender = QPlainTextEdit()
        self.info_layout = QGridLayout()
        self.info_layout.addWidget(self.profile_name_label, 0, 0)
        self.info_layout.addWidget(self.profile_name, 0, 1)
        self.info_layout.addWidget(self.current_weight_label, 1, 0)
        self.info_layout.addWidget(self.current_weight, 1, 1)
        self.info_layout.addWidget(self.goal_weight_label, 2, 0)
        self.info_layout.addWidget(self.goal_weight, 2, 1)
        self.info_layout.addWidget(self.age_label, 3, 0)
        self.info_layout.addWidget(self.age, 3, 1)
        self.info_layout.addWidget(self.activity_level_label, 4, 0)
        self.info_layout.addWidget(self.activity_level, 4, 1)
        self.info_layout.addWidget(self.height_label, 5, 0)
        self.info_layout.addWidget(self.height_, 5, 1)
        self.info_layout.addWidget(self.gender_label, 6, 0)
        self.info_layout.addWidget(self.gender, 6, 1)
        self.layout.addLayout(self.info_layout)

        # Set Up Buttons
        self.button_layout = QGridLayout()
        self.update_button = QPushButton("Update")
        self.cancel_button = QPushButton("Cancel")
        self.button_layout.addWidget(self.update_button, 0, 0)
        self.button_layout.addWidget(self.cancel_button, 0, 1)
        self.layout.addLayout(self.button_layout)

    
