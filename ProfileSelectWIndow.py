
"""
Will Improve UI later.  
"""

import qdarkstyle, sys, csv, main, ModifyProfileWindow, MainWindow
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QComboBox
from pathlib import Path

class ProfileSelectWindow(QMainWindow):
    def __init__(self, profileName):
        super().__init__()

        # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Settings - Health Calculator")
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
        locationOfUser = None
        for index, profile in enumerate(profiles):
            if profileName == profile:
                locationOfUser = index
            self.profile_select_dropdown.addItem(profile)
        self.profile_select_dropdown.setCurrentIndex(locationOfUser)
        self.profile_select_layout.addWidget(self.profile_select_label, 0, 0)
        self.profile_select_layout.addWidget(self.profile_select_dropdown, 0, 1)
        self.profile_select_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Create Buttons
        self.button_layout = QGridLayout()
        self.load_profile_button = QPushButton("Load Profile")
        self.create_profile_button = QPushButton("Create Profile")
        self.delete_profile_button = QPushButton("Delete Profile")
        self.button_layout.addWidget(self.load_profile_button, 0, 0)
        self.button_layout.addWidget(self.create_profile_button, 0, 1)
        self.button_layout.addWidget(self.delete_profile_button, 0, 2)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addLayout(self.button_layout)
        self.layout.addLayout(self.profile_select_layout)

        self.load_profile_button.clicked.connect(self.load_profile)
        self.create_profile_button.clicked.connect(self.go_to_profile_creation)
        self.delete_profile_button.clicked.connect(self.deleteProfile)
    
    def getProfiles(self):
        profilesExist = main.Main.profilesExist()
        if profilesExist[0] == True:
            return profilesExist[1]
        else:
            main.Main.startingProcess()
            #self.close()

    def deleteProfile(self):
        name = self.profile_select_dropdown.currentText()
        newProfiles = []
        with open("profiles.csv", "r", newline="") as profilesText:
            profileLines = profilesText.readlines()
            for profile in profileLines:
                if profile.split(",")[0] != name:
                    newProfiles.append(profile)
        newProfiles[-1] = newProfiles[-1][:-2]
        for index, profile in enumerate(newProfiles):
            if profile == "":
                newProfiles.pop(index)
        with open("profiles.csv", "w", newline="") as profilesWriter:
            profilesWriter.write("".join(newProfiles))

        if (len(newProfiles) > 1):
            self.refreshScr = ProfileSelectWindow(newProfiles[1].split(",")[0])
            self.refreshScr.show()
        else:
            self.newProfile = ModifyProfileWindow.ModifyProfileWindow([False, []])
            self.newProfile.show()

        self.close()
    
    def load_profile(self):
        self.profile_to_load = self.profile_select_dropdown.currentText()

        self.mainWindow = MainWindow.MainWindow(self.profile_to_load)
        self.mainWindow.show()

        self.close()

    def go_to_profile_creation(self):
        self.profileCreate = ModifyProfileWindow.ModifyProfileWindow([False, [None]])
        self.profileCreate.show()

        self.close()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = ProfileSelectWindow("Chris")
    window.show()

    app.exec() 