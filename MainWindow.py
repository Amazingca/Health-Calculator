
# Python syntax is gross and I feel gross.

"""
PyQt Terminology:
-Signal: notification emitted by widget when something happens (.connect())
-Slots: receivers of signals (.connect(reciever))
-event: every interaction the user has with a Qt Application is a kind of event (event Object)
"""

import ModifyProfileWindow, ProfileSelectWindow, CheckInWindow, ProfileData, ProgressGraphWindow, qdarkstyle, webbrowser
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self, profile_name):
        super().__init__()

        self.profile_name = profile_name
        self.profile_data = ProfileData.ProfileData(profile_name)

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
        self.update_button.clicked.connect(self.change_to_modify_profile)
        self.history_button = QPushButton("History")
        self.history_button.clicked.connect(self.open_history_graph)
        self.workouts_button = QPushButton("Workouts")
        self.workouts_button.clicked.connect(self.open_webpage)
        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.change_to_settings)
        self.top_button_layout.addWidget(self.update_button, 0, 0)
        self.top_button_layout.addWidget(self.history_button, 0, 1)
        self.top_button_layout.addWidget(self.workouts_button, 0, 2)
        self.top_button_layout.addWidget(self.settings_button, 0, 3)
        self.layout.addLayout(self.top_button_layout)

        # Set Up Header Greeting
        self.header = QLabel("<b>Welcome, " + profile_name + "<b>") # Insert name from .csv here
        self.layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Set up date + current weight + goal weight fields
        self.weight_layout = QGridLayout()
        self.current_date = QLabel("<b>Current Date<b>: " + self.profile_data.today_date)
        self.current_weight_label = QLabel("<b>Current Weight:<b> " + str(self.profile_data.current_weight) + " lbs")
        self.goal_weight_label = QLabel("<b>Goal Weight:<b> " + str(self.profile_data.goal_weight) + " lbs")
        self.weight_layout.addWidget(self.current_date, 0, 0)
        self.weight_layout.addWidget(self.current_weight_label, 0, 1)
        self.weight_layout.addWidget(self.goal_weight_label, 0, 2)
        self.weight_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.weight_layout)

        # Set up Data Fields (Macros, Vitamins, Minerals)
        self.macro_layout = QGridLayout()
        self.macro_tdee = QPlainTextEdit("TDEE: " + str(self.profile_data.calc_tdee()) + " cals")
        self.macro_tdee.setReadOnly(True)
        self.macro_target_calories = QPlainTextEdit("Target Calories: " + str(self.profile_data.calc_target_cals()) + " cals")
        self.macro_target_calories.setReadOnly(True)
        self.macro_target_protein = QPlainTextEdit("Protein: " + str(self.profile_data.calc_target_protein()) + "g")
        self.macro_target_protein.setReadOnly(True)
        self.macro_target_fat = QPlainTextEdit("Fat: " + str(self.profile_data.calc_target_fat()) + "g")
        self.macro_target_fat.setReadOnly(True)
        self.macro_target_carbs = QPlainTextEdit("Carbs: " + str(self.profile_data.calc_target_carbs()) + "g")
        self.macro_target_carbs.setReadOnly(True)
        self.macro_layout.addWidget(self.macro_tdee, 0, 0)
        self.macro_layout.addWidget(self.macro_target_calories, 0, 1)
        self.macro_layout.addWidget(self.macro_target_protein, 0, 2)
        self.macro_layout.addWidget(self.macro_target_fat, 0, 3)
        self.macro_layout.addWidget(self.macro_target_carbs, 0, 4)
        self.layout.addLayout(self.macro_layout)

        self.vitamin_layout = QGridLayout()
        self.vitamin_A = QPlainTextEdit("Vitamin A: " + str(self.profile_data.calc_target_vitmain_A()) + " mcg RAE")
        self.vitamin_A.setReadOnly(True)
        self.vitamin_C = QPlainTextEdit("Vitamin C: " + str(self.profile_data.calc_target_vitmain_C()) + " mg")
        self.vitamin_C.setReadOnly(True)
        self.vitamin_D = QPlainTextEdit("Vitamin D: " + str(self.profile_data.calc_target_vitamin_D()) + " mcg")
        self.vitamin_D.setReadOnly(True)
        self.vitamin_B6 = QPlainTextEdit("Vitamin B6: " + str(self.profile_data.calc_target_vitamin_B6()) + " mg")
        self.vitamin_B6.setReadOnly(True)
        self.vitamin_E = QPlainTextEdit("Vitamin E: " + str(self.profile_data.calc_target_vitmain_E()) + " mg")
        self.vitamin_E.setReadOnly(True)
        self.vitamin_K = QPlainTextEdit("Vitamin K: " + str(self.profile_data.calc_target_vitmain_K()) + " mcg")
        self.vitamin_K.setReadOnly(True)
        self.vitamin_thiamin = QPlainTextEdit("Thiamin: " + str(self.profile_data.calc_target_vitamin_thiamin()) + " mg")
        self.vitamin_thiamin.setReadOnly(True)
        self.vitamin_B12 = QPlainTextEdit("Vitamin B12: " + str(self.profile_data.calc_target_vitmain_B12()) + " mcg")
        self.vitamin_B12.setReadOnly(True)
        self.vitamin_riboflavin = QPlainTextEdit("Riboflavin: " + str(self.profile_data.calc_target_vitamin_riboflavin()) + " mg")
        self.vitamin_riboflavin.setReadOnly(True)
        self.vitamin_folate = QPlainTextEdit("Folate: " + str(self.profile_data.calc_target_vitmain_folate()) + " mcg DFE")
        self.vitamin_folate.setReadOnly(True)
        self.vitamin_niacin = QPlainTextEdit("Niacin: " + str(self.profile_data.calc_target_vitamin_niacin()) + " mg NE")
        self.vitamin_niacin.setReadOnly(True)
        self.vitamin_choline = QPlainTextEdit("Choline: " + str(self.profile_data.calc_target_vitamin_choline()) + " mg")
        self.vitamin_choline.setReadOnly(True)
        self.vitamin_pantothenic_acid = QPlainTextEdit("Pantothenic Acid: " + str(self.profile_data.calc_target_vitamin_pantothenic_acid()) + " mg")
        self.vitamin_pantothenic_acid.setReadOnly(True)
        self.vitamin_biotin = QPlainTextEdit("Biotin: " + str(self.profile_data.calc_target_vitamin_biotin()) + " mcg")
        self.vitamin_biotin.setReadOnly(True)    
        self.vitamin_carotenoids = QPlainTextEdit("Carotenoids: " + str(self.profile_data.calc_target_vitamin_carotenoids()) + " mcg RAE")
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
        self.mineral_calcium = QPlainTextEdit("Calcium: " + str(self.profile_data.calc_target_mineral_calcium()) + " mg")
        self.mineral_calcium.setReadOnly(True)
        self.mineral_chloride = QPlainTextEdit("Chloride: " + str(self.profile_data.calc_target_mineral_chloride()) + " g")
        self.mineral_chloride.setReadOnly(True)
        self.mineral_chromium = QPlainTextEdit("Chromium: " + str(self.profile_data.calc_target_mineral_chromium()) + " mcg")
        self.mineral_chromium.setReadOnly(True)
        self.mineral_copper = QPlainTextEdit("Copper: " + str(self.profile_data.calc_target_mineral_copper()) + " mcg")
        self.mineral_copper.setReadOnly(True)
        self.mineral_fluoride = QPlainTextEdit("Fluoride: " + str(self.profile_data.calc_target_mineral_fluoride()) + " mg")
        self.mineral_fluoride.setReadOnly(True)
        self.mineral_iodine = QPlainTextEdit("Iodine: " + str(self.profile_data.calc_target_mineral_fluoride()) + " mcg")
        self.mineral_iodine.setReadOnly(True)
        self.mineral_iron = QPlainTextEdit("Iron: " + str(self.profile_data.calc_target_mineral_iron()) + " mg")
        self.mineral_iron.setReadOnly(True)
        self.mineral_magnesium = QPlainTextEdit("Magnesium: " + str(self.profile_data.calc_target_mineral_magnesium()) + " mg")
        self.mineral_magnesium.setReadOnly(True)
        self.mineral_manganese = QPlainTextEdit("Manganese: " + str(self.profile_data.calc_target_mineral_manganese()) + " mg")
        self.mineral_manganese.setReadOnly(True)
        self.mineral_molybdenum = QPlainTextEdit("Molybdenum: " + str(self.profile_data.calc_target_mineral_molybdenum()) + " mcg")
        self.mineral_molybdenum.setReadOnly(True)
        self.mineral_phosphorous = QPlainTextEdit("Phosphorous: " + str(self.profile_data.calc_target_mineral_phosphorous()) + " mg")
        self.mineral_phosphorous.setReadOnly(True)
        self.mineral_potassium = QPlainTextEdit("Potassium: " + str(self.profile_data.calc_target_mineral_potassium()) + " g")
        self.mineral_potassium.setReadOnly(True)
        self.mineral_selenium = QPlainTextEdit("Selenium: " + str(self.profile_data.calc_target_mineral_selenium()) + " mcg")
        self.mineral_selenium.setReadOnly(True)
        self.mineral_sodium = QPlainTextEdit("Sodium: " + str(self.profile_data.calc_target_mineral_sodium()) + " mg")
        self.mineral_sodium.setReadOnly(True)
        self.mineral_zinc = QPlainTextEdit("Zinc: " + str(self.profile_data.calc_target_mineral_sodium()) + " mg")
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
        self.check_in_button.clicked.connect(self.change_to_check_in)
        self.bottom_button_layout.addWidget(self.check_in_button)
        self.layout.addLayout(self.bottom_button_layout)
    
    def change_to_modify_profile(self):
        self.modificationView = ModifyProfileWindow.ModifyProfileWindow([True, [self.profile_name]])
        self.modificationView.show()
        self.close()

    def change_to_settings(self):
        self.settingsView = ProfileSelectWindow.ProfileSelectWindow()
        self.settingsView.show()
        self.close()

    def change_to_check_in(self):
        self.checkInView = CheckInWindow.CheckInWindow(self.profile_name, self.profile_data.today_date)
        self.checkInView.show()
        self.close()

    def open_webpage(self):
        webbrowser.open("https://liftvault.com/search/")

    def open_history_graph(self):
        self.historyGraphView = ProgressGraphWindow.ProgressGraphWindow(self.profile_name)
        self.historyGraphView.show()