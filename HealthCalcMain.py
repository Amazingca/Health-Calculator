
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

        # Populate Primary Data Fields (imperial -- metric is used within formulas, and these conversions take place within functions)
        self.profile_name = profile_name
        self.current_weight = 0
        self.goal_weight = 0
        self.age = 0
        self.activity_level = 0
        self.activity_level_multiplier = 0
        self.height_ = 0
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
        self.header = QLabel("<b>Welcome, " + self.profile_name + "<b>") # Insert name from .csv here
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
        self.macro_target_calories = QPlainTextEdit("Target Calories: " + str(self.calc_target_cals()) + " cals")
        self.macro_target_calories.setReadOnly(True)
        self.macro_target_protein = QPlainTextEdit("Protein: " + str(self.calc_target_protein()) + "g")
        self.macro_target_protein.setReadOnly(True)
        self.macro_target_fat = QPlainTextEdit("Fat: " + str(self.calc_target_fat()) + "g")
        self.macro_target_fat.setReadOnly(True)
        self.macro_target_carbs = QPlainTextEdit("Carbs: " + str(self.calc_target_carbs()) + "g")
        self.macro_target_carbs.setReadOnly(True)
        self.macro_layout.addWidget(self.macro_tdee, 0, 0)
        self.macro_layout.addWidget(self.macro_target_calories, 0, 1)
        self.macro_layout.addWidget(self.macro_target_protein, 0, 2)
        self.macro_layout.addWidget(self.macro_target_fat, 0, 3)
        self.macro_layout.addWidget(self.macro_target_carbs, 0, 4)
        self.layout.addLayout(self.macro_layout)

        self.vitamin_layout = QGridLayout()
        self.vitamin_A = QPlainTextEdit("Vitamin A: " + str(self.calc_target_vitmain_A()) + " mcg RAE")
        self.vitamin_A.setReadOnly(True)
        self.vitamin_C = QPlainTextEdit("Vitamin C: " + str(self.calc_target_vitmain_C()) + " mg")
        self.vitamin_C.setReadOnly(True)
        self.vitamin_D = QPlainTextEdit("Vitamin D: " + str(self.calc_target_vitamin_D()) + " mcg")
        self.vitamin_D.setReadOnly(True)
        self.vitamin_B6 = QPlainTextEdit("Vitamin B6: " + str(self.calc_target_vitamin_B6()) + " mg")
        self.vitamin_B6.setReadOnly(True)
        self.vitamin_E = QPlainTextEdit("Vitamin E: " + str(self.calc_target_vitmain_E()) + " mg")
        self.vitamin_E.setReadOnly(True)
        self.vitamin_K = QPlainTextEdit("Vitamin K: " + str(self.calc_target_vitmain_K()) + " mcg")
        self.vitamin_K.setReadOnly(True)
        self.vitamin_thiamin = QPlainTextEdit("Thiamin: " + str(self.calc_target_vitamin_thiamin()) + " mg")
        self.vitamin_thiamin.setReadOnly(True)
        self.vitamin_B12 = QPlainTextEdit("Vitamin B12: " + str(self.calc_target_vitmain_B12()) + " mcg")
        self.vitamin_B12.setReadOnly(True)
        self.vitamin_riboflavin = QPlainTextEdit("Riboflavin: " + str(self.calc_target_vitamin_riboflavin()) + " mg")
        self.vitamin_riboflavin.setReadOnly(True)
        self.vitamin_folate = QPlainTextEdit("Folate: " + str(self.calc_target_vitmain_folate()) + " mcg DFE")
        self.vitamin_folate.setReadOnly(True)
        self.vitamin_niacin = QPlainTextEdit("Niacin: " + str(self.calc_target_vitamin_niacin()) + " mg NE")
        self.vitamin_niacin.setReadOnly(True)
        self.vitamin_choline = QPlainTextEdit("Choline: " + str(self.calc_target_vitamin_choline()) + " mg")
        self.vitamin_choline.setReadOnly(True)
        self.vitamin_pantothenic_acid = QPlainTextEdit("Pantothenic Acid: " + str(self.calc_target_vitamin_pantothenic_acid()) + " mg")
        self.vitamin_pantothenic_acid.setReadOnly(True)
        self.vitamin_biotin = QPlainTextEdit("Biotin: " + str(self.calc_target_vitamin_biotin()) + " mcg")
        self.vitamin_biotin.setReadOnly(True)    
        self.vitamin_carotenoids = QPlainTextEdit("Carotenoids: " + str(self.calc_target_vitamin_carotenoids()) + " mcg RAE")
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

            current_weight_kg = self.current_weight * 0.45359237
            height_cm = self.height_ * 2.54

            if self.gender == "m":
                self.bmr = ((10 * current_weight_kg) + (6.25 * height_cm) - (5 * self.age) + 5)
            else:
                self.bmr = ((10 * current_weight_kg) + (6.25 * height_cm) - (5 * self.age) - 161)
            
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
    
    def calc_target_cals(self):
        if self.current_weight < self.goal_weight:
            return self.calc_tdee() + 300
        elif self.current_weight > self.goal_weight:
            return self.calc_tdee() - 300
        else:
            return self.calc_tdee()
    
    def calc_target_protein(self):
        return (self.calc_tdee() * 0.25) // 4
    
    def calc_target_carbs(self):
        return (self.calc_tdee() * 0.45) // 4

    def calc_target_fat(self):
        return (self.calc_tdee() * 0.25) // 9        

    def calc_target_vitmain_A(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/
        # Returns mcg dose
        
        if self.age < 4: return 300
        elif self.age < 9: return 400
        elif self.age < 14: return 600
        else:
            if self.gender == "m": return 900
            else: return 700

    def calc_target_vitmain_C(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/
        # Returns mg dose

        if self.age < 4: return 15
        elif self.age < 9: return 25
        elif self.age < 14: return 45
        elif self.age < 19:
            if self.gender == "m": return 75
            else: return 65
        else:
            if self.gender == "m": return 90
            else: return 75

    def calc_target_vitamin_D(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/
        # Returns mcg dose

        if self.age < 70: return 15
        else: return 20

    def calc_target_vitamin_B6(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminB6-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 1.0
        elif self.age < 19:
            if self.gender == "m": return 1.3
            else: return 1.2
        elif self.age < 51: return 1.3
        else: 
            if self.gender == "m": return 1.7
            else: return 1.5

    def calc_target_vitmain_E(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 6
        elif self.age < 9: return 7
        elif self.age < 14: return 11
        else: return 15

    def calc_target_vitmain_K(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 30
        elif self.age < 9: return 55
        elif self.age < 14: return 60
        elif self.age < 19: return 75
        else:
            if self.gender == "m": return 120
            else: return 90

    def calc_target_vitamin_thiamin(self):
        # Source: https://ods.od.nih.gov/factsheets/Thiamin-HealthProfessional/
        # Returns measurement in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 0.9
        elif self.age < 19:
            if self.gender == "m": return 1.2
            else: return 1.0
        else:
            if self.gender == "m": return 1.2
            else: return 1.1

    def calc_target_vitmain_B12(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 0.9
        elif self.age < 9: return 1.2
        elif self.age < 14: return 1.8
        else: return 2.4

    def calc_target_vitamin_riboflavin(self):
        # Source: https://ods.od.nih.gov/factsheets/Riboflavin-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 0.9
        elif self.age < 19:
            if self.gender == "m": return 1.3
            else: return 1.0
        else:
            if self.gender == "m": return 1.3
            else: return 1.1
        
    def calc_target_vitmain_folate(self):
        # https://ods.od.nih.gov/factsheets/Folate-HealthProfessional/
        # Returns dose in mcg DFE

        if self.age < 4: return 150
        elif self.age < 9: return 200
        elif self.age < 14: return 300
        else: return 400

    def calc_target_vitamin_niacin(self):
        # Source: https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/
        # Returns dose in mg NE

        if self.age < 4: return 6
        elif self.age < 9: return 8
        elif self.age < 14: return 12
        else:
            if self.gender == "m": return 16
            else: return 14

    def calc_target_vitamin_choline(self):
        # Source: https://ods.od.nih.gov/factsheets/Choline-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 200
        elif self.age < 9: return 250
        elif self.age < 14: return 375
        elif self.age < 19:
            if self.gender == "m": return 550
            else: return 400
        else:
            if self.gender == "m": return 550
            else: return 425
            
    def calc_target_vitamin_pantothenic_acid(self):
        # Source: https://ods.od.nih.gov/factsheets/PantothenicAcid-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 2
        elif self.age < 9: return 3
        elif self.age < 14: return 4
        else: return 5

    def calc_target_vitamin_biotin(self):
        # Source: https://ods.od.nih.gov/factsheets/Biotin-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 8
        elif self.age < 9: return 12
        elif self.age < 14: return 20
        elif self.age < 19: return 25
        else: return 30

    def calc_target_vitamin_carotenoids(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/
        # Returns dose in mcg RAE

        if self.age < 4: return 300
        elif self.age < 9: return 400
        elif self.age < 14: return 600
        else:
            if self.gender == "m": return 900
            else: return 700

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow("chris")
    window.show()

    app.exec() 

