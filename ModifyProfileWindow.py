import MainWindow, ProfileData
import qdarkstyle, sys, csv
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class ModifyProfileWindow(QMainWindow):
    def __init__(self, isNew):
        super().__init__()

        existingProfile = ()
        if isNew == False:
            existingProfile = ProfileData.ProfileData("chris").build_from_profile(True)

        # Set Up Window Title (with conditional), Size, and Style (Dark)
        if isNew:
            self.setWindowTitle("Welcome - Health Calculator")
        else:
            self.setWindowTitle("Update - Health Calculator")
        # Last fixed dimensions: 300, 450
        self.setFixedSize(QSize(300, 500))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set Up Layout of Window 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Header grid layout, with modification conditional
        if isNew:
            self.header = QLabel("<b>Add a New Profile<b>")
        else:
            self.header = QLabel("<b>Modify Profile")
        self.layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        # Name grid layout, with modification conditional
        self.name_layout = QGridLayout()
        self.name_input = QLineEdit(self)
        if isNew:
            self.name_text = QLabel("<b>Enter your name:<b>")
        else:
            self.name_text = QLabel("<b>Change your name:<b>")
            self.name_input.setText(existingProfile[0])
        self.name_layout.addWidget(self.name_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.name_layout.addWidget(self.name_input, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

        # Biological sex dropdown layout, with modification conditional
        self.bioSex_layout = QGridLayout()
        self.bioSex_dropdown = QComboBox()
        self.bioSex_dropdown.addItems(['Choose', 'Male', 'Female'])
        if isNew:
            self.bioSex_text = QLabel("<b>Choose your biological sex:<b>")
        else:
            self.bioSex_text = QLabel("<b>Change your biological sex:<b>")
            self.bioSex_dropdown.setCurrentText(existingProfile[1].capitalize())
        self.bioSex_layout.addWidget(self.bioSex_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.bioSex_layout.addWidget(self.bioSex_dropdown, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

        # Age grid layout, with modification conditional
        self.age_layout = QGridLayout()
        self.age_input = QLineEdit(self)
        if isNew:
            self.age_text = QLabel("<b>Enter your age:<b>")
        else:
            self.age_text = QLabel("<b>Change your age:<b>")
            self.age_input.setText(f"{existingProfile[2]}")
        self.age_layout.addWidget(self.age_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.age_layout.addWidget(self.age_input, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

        # currentWeight grid layout, with modification conditional
        self.currentWeight_layout = QGridLayout()
        self.currentWeight_input = QLineEdit(self)
        if isNew:
            self.currentWeight_text = QLabel("<b>Enter your weight:<b>")
        else:
            self.currentWeight_text = QLabel("<b>Change your weight:<b>")
            self.currentWeight_input.setText(f"{existingProfile[3]}")
        self.currentWeight_layout.addWidget(self.currentWeight_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.currentWeight_layout.addWidget(self.currentWeight_input, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

        # currentWeight grid layout, with modification conditional
        self.goalWeight_layout = QGridLayout()
        self.goalWeight_input = QLineEdit(self)
        if isNew:
            self.goalWeight_text = QLabel("<b>Enter your goal:<b>")
        else:
            self.goalWeight_text = QLabel("<b>Change your goal:<b>")
            self.goalWeight_input.setText(f"{existingProfile[4]}")
        self.currentWeight_layout.addWidget(self.goalWeight_text, 0, 1, alignment=Qt.AlignmentFlag.AlignBottom)
        self.currentWeight_layout.addWidget(self.goalWeight_input, 1, 1, alignment=Qt.AlignmentFlag.AlignTop)

        # Height prid layout, with modification conditional
        self.height_layout = QGridLayout()
        self.feetHeight_input = QLineEdit(self)
        self.inchesHeight_input = QLineEdit(self)
        if isNew:
            self.height_text = QLabel("<b>Enter your height:<b>")
        else:
            self.height_text = QLabel("<b>Change your height:<b>")
            feet = existingProfile[5] // 12
            inches = existingProfile[5] % 12
            self.feetHeight_input.setText(f"{feet}")
            self.inchesHeight_input.setText(f"{inches}")
        self.height_layout.addWidget(self.height_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        # Feet sub-layout
        self.heightFeet_layout = QGridLayout()
        self.feetHeight_text = QLabel("<b>ft<b>")
        self.heightFeet_layout.addWidget(self.feetHeight_input, 0, 0)
        self.heightFeet_layout.addWidget(self.feetHeight_text, 0, 1)
        self.height_layout.addLayout(self.heightFeet_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)
        # Inches sublayout
        self.heightInches_layout = QGridLayout()
        self.inchesHeight_text = QLabel("<b>in<b>")
        self.heightInches_layout.addWidget(self.inchesHeight_input, 0, 0)
        self.heightInches_layout.addWidget(self.inchesHeight_text, 0, 1)
        self.height_layout.addLayout(self.heightInches_layout, 1, 1, alignment=Qt.AlignmentFlag.AlignTop)

        # Acitivity level layout, with modification conditional
        self.activity_layout = QGridLayout()
        self.activitySlider_layout = QGridLayout()
        self.activity_slider = QSlider(Qt.Horizontal, self)
        self.activity_slider.setMinimum(0)
        self.activity_slider.setMaximum(4)
        self.activity_slider.setTickInterval(1)
        self.activity_slider.setSingleStep(1)
        if isNew:
            self.activity_text = QLabel("<b>Choose your activity level:<b>")
        else:
            self.activity_text = QLabel("<b>Change your activity level:<b>")
            self.activity_slider.setSliderPosition(existingProfile[6])
        self.activity_layout.addWidget(self.activity_text, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.activitySlider_layout.addWidget(self.activity_slider, 0, 0)
        self.sliderText_layout = QGridLayout()
        self.sliderTextOne_layout = QGridLayout()
        self.sliderText_one = QLabel("<b>0<b>")
        self.sliderText_layout.addWidget(self.sliderText_one, 0, 0)
        self.sliderText_four = QLabel("<b>4<b>")
        self.sliderText_layout.addWidget(self.sliderText_four, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.activitySlider_layout.addLayout(self.sliderText_layout, 1, 0)
        self.activity_layout.addLayout(self.activitySlider_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

        # Add grid views to main layout
        self.layout.addLayout(self.name_layout)
        self.layout.addLayout(self.bioSex_layout)
        self.layout.addLayout(self.age_layout)
        self.layout.addLayout(self.currentWeight_layout)
        self.layout.addLayout(self.height_layout)
        self.layout.addLayout(self.activity_layout)

        # Create Update or Cancel button based on modification conditional
        self.modifyButton_layout = QGridLayout()
        if isNew:
            self.modify_button = QPushButton("Create")
            self.modifyButton_layout.addWidget(self.modify_button)
        else:
            self.modify_button = QPushButton("Update")
            self.modifyButton_layout.addWidget(self.modify_button, 0, 1)
            self.cancel_button = QPushButton("Cancel")
            self.modifyButton_layout.addWidget(self.cancel_button, 0, 0)
        self.layout.addLayout(self.modifyButton_layout)

        self.modify_button.clicked.connect(self.on_pushButton_clicked)
        self.dialog = MainWindow.MainWindow("chris")

        # Dialog instance in PyQT. Might be useful to show if not all boxes are filled in.
        #info = QMessageBox.information(self, "", "Please fill in the missing categories.")

    # Changes view
    def on_pushButton_clicked(self):
        self.dialog.show()

    # Function that handle profile creation/updating.
    def updateProfile(self, isNew):
        None

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Ternary operator that loads display based on whether input is "true" or "false".
    isNew = True if input("New profile? (true/false)\n>>> ").lower() == "true" else False
    
    window = ModifyProfileWindow(isNew)
    window.show()

    app.exec() 