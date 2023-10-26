
import MainWindow, qdarkstyle, sys, csv, datetime
import pyqtgraph as pg
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot 
from matplotlib.dates import date2num

class ProgressGraphWindow(QMainWindow):
    def __init__(self, profile_name, *args, **kwargs):
        super(ProgressGraphWindow, self).__init__(*args, **kwargs)

        self.profile_name = profile_name

        # Pull Graph Data from .csv
        self.dates_and_weights = self.get_initial_data() # [[dates], [weights]]

        # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health Calculator Demo")
        self.setFixedSize(QSize(1000, 800))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set up Graph
        self.graphWidget = pg.PlotWidget()
        self.date_axis = pg.DateAxisItem(orientation="bottom")
        self.graphWidget.setAxisItems({'bottom':self.date_axis})

        self.graphWidget.setLabel('left', 'Weight (lb)')
        self.graphWidget.setLabel('bottom', 'Date')
        self.graphWidget.setTitle('Weight Progress Over Time')
        self.setCentralWidget(self.graphWidget)

        self.plot_data()

    def get_initial_data(self):

        dates_and_weights = [[], []]
 
        with open("profiles_TEST.csv", 'r', newline='') as profile: 
            csv_reader = csv.reader(profile)
        
            for row in csv_reader:
                if row[0] == self.profile_name: 
                    column = 7 # Where data entries begin
                    while column < len(row):
                        current_cell_data = row[column].split(".") # Date.Weight Format
                        dates_and_weights[0].append(datetime.datetime.strptime(current_cell_data[0], "%m/%d/%Y"))
                        dates_and_weights[1].append(int(current_cell_data[1]))
                        column += 1
        
        return dates_and_weights

    def plot_data(self):
        
        x = date2num(self.dates_and_weights[0])  # Convert dates to numeric values
        y = self.dates_and_weights[1]
        
        scatter = pg.ScatterPlotItem(x=x, y=y, size=5, pen=pg.mkPen(None))
        self.graphWidget.addItem(scatter)
        self.graphWidget.getAxis("bottom").setStyle(tickTextOffset=20)
        self.graphWidget.getAxis("bottom").setTextPen("w")
        self.graphWidget.getAxis("bottom").setPen("w")
        self.graphWidget.getAxis("bottom").setLabel("Date", color=(255, 255, 255))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressGraphWindow("Chris")        
    window.show()
    app.exec() 
