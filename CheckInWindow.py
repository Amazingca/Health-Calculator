
import MainWindow, qdarkstyle, sys, csv
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QGridLayout

class CheckInWindow(QMainWindow):
    def __init__(self, profile_name, today_date):
        super().__init__()

        self.profile_name = profile_name
        self.today_date = today_date

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
        self.window_message_label = QLabel()
        self.current_weight_label = QLabel("Current Weight (lb)")
        self.current_weight_box = QPlainTextEdit()
        self.current_weight_box.setMinimumHeight(30) 
        self.current_weight_box.setMaximumHeight(30)
        self.info_layout.addWidget(self.current_weight_label, 0, 0)
        self.info_layout.addWidget(self.current_weight_box, 0, 1)
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.window_message_label)
        self.layout.addLayout(self.info_layout)

        # Set Up Buttons
        self.button_layout = QGridLayout()
        self.update_button = QPushButton("Check In")
        self.update_button.clicked.connect(self.check_in)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)
        self.button_layout.addWidget(self.update_button, 0, 0)
        self.button_layout.addWidget(self.cancel_button, 0, 1)
        self.layout.addLayout(self.button_layout)

    def check_in(self):

        try:
            if not self.current_weight_box.toPlainText().isdigit():
                raise TypeError("Invalid Entry")
            else:
                self.current_weight = self.current_weight_box.toPlainText()

                with open("profiles.csv", 'r', newline='') as profile:
                    csv_reader = csv.reader(profile)
                    csv_data = []

                    for row in csv_reader:
                        if row[0] == self.profile_name:
                            updated_row = row[0:-1] # Remove Empty Space
                            updated_row.append(self.today_date + "." + self.current_weight)
                            csv_data.append(updated_row)
                        else:
                            csv_data.append(row)
                    
                with open("profiles.csv", 'w', newline='') as profile:
                    csv_writer = csv.writer(profile)
                    csv_writer.writerows(csv_data)
                
                self.window_message_label.setText("Success.  Press Cancel to return.") 
                self.update_button.setEnabled(False)

        except TypeError as error:
            self.window_message_label.setText(str(error))

   
    def cancel(self):
        self.return_window = MainWindow.MainWindow(self.profile_name)
        self.return_window.show()
        self.close()


