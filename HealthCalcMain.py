
# Python syntax is gross and I feel gross.

"""
PyQt Terminology:
-Signal: notification emitted by widget when something happens (.connect())
-Slots: receivers of signals (.connect(reciever))
-event: every interaction the user has with a Qt Application is a kind of event (event Object)
"""

import sys, csv, datetime, qdarkstyle
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self, profile_name):
        super().__init__()

        # Populate Primary Data Fields 
        self.profile_name = profile_name
        self.current_weight = 0
        self.current_weight_kg = 0
        self.goal_weight = 0
        self.goal_weight_kg = 0
        self.age = 0
        self.activity_level = 0
        self.activity_level_multiplier = 0
        self.height_ = 0
        self.height_cm = 0
        self.gender = None
        self.bmr = 0
        self.today_date = datetime.date.today().strftime("%m/%d/%Y")
        self.build_from_profile()

        # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health Calculator Demo")
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set Up Layout of Window 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create Buttons
        self.top_button_layout = QGridLayout()
        self.update_button = QPushButton("Update Info")
        self.history_button = QPushButton("History")
        self.workouts_button = QPushButton("Workouts")
        self.settings_button = QPushButton("Settings")
        self.top_button_layout.addWidget(self.update_button, 0, 0)
        self.top_button_layout.addWidget(self.history_button, 0, 1)
        self.top_button_layout.addWidget(self.workouts_button, 0, 2)
        self.top_button_layout.addWidget(self.settings_button, 0, 3)
        self.layout.addLayout(self.top_button_layout)

        # Set Up Header Greeting
        self.header = QLabel("<b>Welcome " + self.profile_name + "<b>") # Insert name from .csv here
        self.layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Set up date + current weight + goal weight fields
        self.weight_layout = QGridLayout()
        self.current_date = QLabel("<b>Current Date<b>: " + self.today_date)
        self.current_weight_label = QLabel("<b>Current Weight:<b> " + str(self.current_weight) + " lbs")
        self.goal_weight_label = QLabel("<b>Goal Weight:<b> " + str(self.goal_weight) + " lbs")
        self.weight_layout.addWidget(self.current_date, 0, 0)
        self.weight_layout.addWidget(self.current_weight_label, 0, 1)
        self.weight_layout.addWidget(self.goal_weight_label, 0, 2)
        self.weight_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.weight_layout)

        # Set up Data Fields (Macros, Vitamins, Minerals)
        self.macro_layout = QGridLayout()
        self.macro_tdee = QPlainTextEdit("TDEE: " + str(self.calc_tdee()) + " cals")
        self.macro_tdee.setReadOnly(True)
        self.macro_target_calories = QPlainTextEdit("Target Calories: ")
        self.macro_target_calories.setReadOnly(True)
        self.macro_target_protein = QPlainTextEdit("Protein: ")
        self.macro_target_protein.setReadOnly(True)
        self.macro_target_fat = QPlainTextEdit("Fat: ")
        self.macro_target_fat.setReadOnly(True)
        self.macro_target_carbs = QPlainTextEdit("Carbs: ")
        self.macro_target_carbs.setReadOnly(True)
        self.macro_layout.addWidget(self.macro_tdee, 0, 0)
        self.macro_layout.addWidget(self.macro_target_calories, 0, 1)
        self.macro_layout.addWidget(self.macro_target_protein, 0, 2)
        self.macro_layout.addWidget(self.macro_target_fat, 0, 3)
        self.macro_layout.addWidget(self.macro_target_carbs, 0, 4)
        self.layout.addLayout(self.macro_layout)

        self.vitamin_layout = QGridLayout()
        self.vitamin_A = QPlainTextEdit("Vitamin A: ")
        self.vitamin_A.setReadOnly(True)
        self.vitamin_C = QPlainTextEdit("Vitamin C: ")
        self.vitamin_C.setReadOnly(True)
        self.vitamin_D = QPlainTextEdit("Vitamin D: ")
        self.vitamin_D.setReadOnly(True)
        self.vitamin_B6 = QPlainTextEdit("Vitamin B6: ")
        self.vitamin_B6.setReadOnly(True)
        self.vitamin_E = QPlainTextEdit("Vitamin E: ")
        self.vitamin_E.setReadOnly(True)
        self.vitamin_K = QPlainTextEdit("Vitamin K: ")
        self.vitamin_K.setReadOnly(True)
        self.vitamin_thiamin = QPlainTextEdit("Thiamin: ")
        self.vitamin_thiamin.setReadOnly(True)
        self.vitamin_B12 = QPlainTextEdit("Vitamin B12: ")
        self.vitamin_B12.setReadOnly(True)
        self.vitamin_riboflavin = QPlainTextEdit("Riboflavin: ")
        self.vitamin_A.setReadOnly(True)
        self.vitamin_folate = QPlainTextEdit("Folate: ")
        self.vitamin_folate.setReadOnly(True)
        self.vitamin_niacin = QPlainTextEdit("Niacin: ")
        self.vitamin_niacin.setReadOnly(True)
        self.vitamin_choline = QPlainTextEdit("Choline: ")
        self.vitamin_choline.setReadOnly(True)
        self.vitamin_pantothenic_acid = QPlainTextEdit("Pantothenic Acid: ")
        self.vitamin_pantothenic_acid.setReadOnly(True)
        self.vitamin_biotin = QPlainTextEdit("Biotin: ")
        self.vitamin_biotin.setReadOnly(True)    
        self.vitamin_carotenoids = QPlainTextEdit("Carotenoids: ")
        self.vitamin_carotenoids.setReadOnly(True)
        self.vitamin_layout.addWidget(self.vitamin_A, 0, 0)
        self.vitamin_layout.addWidget(self.vitamin_C, 0, 1)
        self.vitamin_layout.addWidget(self.vitamin_D, 0, 2)
        self.vitamin_layout.addWidget(self.vitamin_B6, 0, 3)
        self.vitamin_layout.addWidget(self.vitamin_E, 0, 4)
        self.vitamin_layout.addWidget(self.vitamin_K, 0, 5)
        self.vitamin_layout.addWidget(self.vitamin_thiamin, 0, 6)
        self.vitamin_layout.addWidget(self.vitamin_B12, 0, 7)
        self.vitamin_layout.addWidget(self.vitamin_riboflavin, 1, 0)
        self.vitamin_layout.addWidget(self.vitamin_folate, 1, 1)
        self.vitamin_layout.addWidget(self.vitamin_niacin, 1, 2)
        self.vitamin_layout.addWidget(self.vitamin_choline, 1, 3)
        self.vitamin_layout.addWidget(self.vitamin_pantothenic_acid, 1, 4)
        self.vitamin_layout.addWidget(self.vitamin_biotin, 1, 5)
        self.vitamin_layout.addWidget(self.vitamin_carotenoids, 1, 6)
        self.layout.addLayout(self.vitamin_layout)
        
        self.mineral_layout = QGridLayout()
        self.mineral_calcium = QPlainTextEdit("Calcium: ")
        self.mineral_calcium.setReadOnly(True)
        self.mineral_chloride = QPlainTextEdit("Chloride: ")
        self.mineral_chloride.setReadOnly(True)
        self.mineral_chromium = QPlainTextEdit("Chromium: ")
        self.mineral_chromium.setReadOnly(True)
        self.mineral_copper = QPlainTextEdit("Copper: ")
        self.mineral_copper.setReadOnly(True)
        self.mineral_fluoride = QPlainTextEdit("Fluoride: ")
        self.mineral_fluoride.setReadOnly(True)
        self.mineral_iodine = QPlainTextEdit("Iodine: ")
        self.mineral_iodine.setReadOnly(True)
        self.mineral_iron = QPlainTextEdit("Iron: ")
        self.mineral_iron.setReadOnly(True)
        self.mineral_magnesium = QPlainTextEdit("Magnesium: ")
        self.mineral_magnesium.setReadOnly(True)
        self.mineral_manganese = QPlainTextEdit("Manganese: ")
        self.mineral_manganese.setReadOnly(True)
        self.mineral_molybdenum = QPlainTextEdit("Molybdenum: ")
        self.mineral_molybdenum.setReadOnly(True)
        self.mineral_phosphorous = QPlainTextEdit("Phosphorous: ")
        self.mineral_phosphorous.setReadOnly(True)
        self.mineral_potassium = QPlainTextEdit("Potassium: ")
        self.mineral_potassium.setReadOnly(True)
        self.mineral_selenium = QPlainTextEdit("Selenium: ")
        self.mineral_selenium.setReadOnly(True)
        self.mineral_sodium = QPlainTextEdit("Sodium: ")
        self.mineral_sodium.setReadOnly(True)
        self.mineral_zinc = QPlainTextEdit("Zinc: ")
        self.mineral_zinc.setReadOnly(True)
        self.mineral_layout.addWidget(self.mineral_calcium, 0, 0)
        self.mineral_layout.addWidget(self.mineral_chloride, 0, 1)
        self.mineral_layout.addWidget(self.mineral_chromium, 0, 2)
        self.mineral_layout.addWidget(self.mineral_copper, 0, 3)
        self.mineral_layout.addWidget(self.mineral_fluoride, 0, 4)
        self.mineral_layout.addWidget(self.mineral_iodine, 0, 5)
        self.mineral_layout.addWidget(self.mineral_iron, 0, 6)
        self.mineral_layout.addWidget(self.mineral_magnesium, 0, 7)
        self.mineral_layout.addWidget(self.mineral_manganese, 1, 0)
        self.mineral_layout.addWidget(self.mineral_molybdenum, 1, 1)
        self.mineral_layout.addWidget(self.mineral_phosphorous, 1, 2)
        self.mineral_layout.addWidget(self.mineral_potassium, 1, 3)
        self.mineral_layout.addWidget(self.mineral_selenium, 1, 4)
        self.mineral_layout.addWidget(self.mineral_sodium, 1, 5)
        self.mineral_layout.addWidget(self.mineral_zinc, 1, 6)
        self.layout.addLayout(self.mineral_layout)

        self.bottom_button_layout = QGridLayout()
        self.check_in_button = QPushButton("Check In")
        self.bottom_button_layout.addWidget(self.check_in_button)
        self.layout.addLayout(self.bottom_button_layout)

    def build_from_profile(self):
        with open("profiles.csv", 'r', newline='') as profile:
            csv_reader = csv.reader(profile)

            for row in csv_reader:
                if row[0] == self.profile_name:
                    self.current_weight = int(row[1])
                    self.goal_weight = int(row[2])
                    self.age = int(row[3])
                    self.activity_level = int(row[4])
                    self.height_ = int(row[5])
                    self.gender = row[6]
                    break

            self.current_weight_kg = self.current_weight * 0.45359237
            self.goal_weight_kg = self.goal_weight * 0.45359237
            self.height_cm = self.height_ * 2.54

            if self.gender == "m":
                self.bmr = ((10 * self.current_weight_kg) + (6.25 * self.height_cm) - (5 * self.age) + 5)
            else:
                self.bmr = ((10 * self.current_weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 161)
            
            self.activity_level_multiplier = self.generate_activity_level_multiplier()
            
    def generate_activity_level_multiplier(self):

        if self.activity_level == 1:
            return 1.375

        elif self.activity_level == 2:
            return 1.55

        elif self.activity_level == 3: 
            return 1.725

        elif self.activity_level == 4:
            return 1.9
        
        else: 
            return 1.2

    def calc_tdee(self):
        return int(self.bmr * self.activity_level_multiplier)
    
    
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow("chris")
    window.show()

    app.exec() 

