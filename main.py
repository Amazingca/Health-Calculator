
import MainWindow
import ModifyProfileWindow
import sys, csv
from PyQt6.QtWidgets import QApplication
from pathlib import Path

if __name__ == "__main__":

    app = QApplication(sys.argv)

    profiles = Path("profiles.csv")
    profilesExist = [False, None] # Array with default False and None for when profiles don't exist. This would otherwise populate with True, and the name of the 2nd row profile if it exists.
    if profiles.is_file():
        with open("profiles.csv") as profileFile:
            profilesReader = csv.reader(profileFile)
            length = 0
            name = None
            for row in profilesReader:
                length += 1
                if length > 1:
                    profilesExist[1] = row[0] # Sets name of user in profile to one that is passed. This will eventually be changed to the profile name that has a most recent indicator.
                print(name)
            # Length greater than 1 (first row is item names), then consider it with profiles.
            if length > 1:
                profilesExist[0] = True
    
    if profilesExist[0]:
        window = MainWindow.MainWindow(profilesExist[1])
    else:
        window = ModifyProfileWindow.ModifyProfileWindow(True)
    
    window.show()

    app.exec() 