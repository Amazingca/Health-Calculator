
import MainWindow
import ModifyProfileWindow
import sys, csv
from PyQt6.QtWidgets import QApplication
from pathlib import Path

class Main:

    # Function used to return a structured array based on profile existence and last used profile.
    def profilesExist():
        
        profiles = Path("profiles.csv")
        profilesExist = [False, []] # Array with default False and None for when profiles don't exist. This would otherwise populate with True, and the name of the 2nd row profile if it exists.
        
        if profiles.is_file():
            with open("profiles.csv") as profileFile:
                profilesReader = csv.reader(profileFile)
                length = 0
                name = None
                for row in profilesReader:
                    length += 1
                    if length > 1:
                        profilesExist[1].append(row[0]) # Adds name of user in profile to subarray in profilesExist. This will eventually be changed to the include the last user as the leading one in the array, assuming there are multiple profiles.
                # Length greater than 1 (first row is item names), then consider it with profiles.
                if length > 1:
                    profilesExist[0] = True
        return profilesExist
    
    # Starting process which runs checks and opens certain windows based on whether profiles exist already.
    def startingProcess():
        
        app = QApplication(sys.argv)

        profilesExist = Main.profilesExist()

        if profilesExist[0]:
            window = MainWindow.MainWindow(profilesExist[1][0])
        else:
            window = ModifyProfileWindow.ModifyProfileWindow(profilesExist)
        
        window.show()
        app.exec() 

if __name__ == "__main__":

    Main.startingProcess()