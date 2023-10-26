
"""
Will Improve UI later.  
"""

import qdarkstyle, sys, csv, main
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QComboBox
from pathlib import Path

class ProfileSelectWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health Calculator Demo")
        self.setFixedSize(QSize(400, 150))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set Up Layout of Window 
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Set Up Drop Down Profile Select
        self.profile_select_layout = QGridLayout()
        self.profile_select_label = QLabel("Select Profile") # Insert name from .csv here
        self.profile_select_dropdown = QComboBox(self)
        profiles = self.getProfiles()
        for profile in profiles:
            self.profile_select_dropdown.addItem(profile)
        self.profile_select_dropdown.setCurrentIndex(0)
        self.profile_select_layout.addWidget(self.profile_select_label, 0, 0)
        self.profile_select_layout.addWidget(self.profile_select_dropdown, 0, 1)
        self.profile_select_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Create Buttons
        self.button_layout = QGridLayout()
        self.load_profile_button = QPushButton("Load Profile")
        self.create_profile_button = QPushButton("Create Profile")
        self.delete_profile_button = QPushButton("Delete Profile")
        self.delete_profile_button.clicked.connect(self.deleteProfile)
        self.button_layout.addWidget(self.load_profile_button, 0, 0)
        self.button_layout.addWidget(self.create_profile_button, 0, 1)
        self.button_layout.addWidget(self.delete_profile_button, 0, 2)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addLayout(self.button_layout)
        self.layout.addLayout(self.profile_select_layout)
    
    def getProfiles(self):
        profilesExist = main.Main.profilesExist()
        if profilesExist[0] == True:
            return profilesExist[1]
        else:
            main.Main.startingProcess()
            #self.close()

    def deleteProfile(self):
        name = self.profile_select_dropdown.currentText()
        with open("profiles.csv", "r") as profilesText:#, open("profiles.csv", "w") as profilesWrite:
            profilesRead = csv.reader(profilesText)
            newProfiles = []
            for index, profile in enumerate(profilesRead):
                if profile[0] != name:
                    newProfiles.append(profile)
            print(newProfiles)
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = ProfileSelectWindow()
    window.show()

    app.exec() 