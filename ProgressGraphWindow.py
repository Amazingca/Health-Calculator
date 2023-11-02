
import qdarkstyle, sys, csv, datetime, time
import pyqtgraph as pg
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow

class ProgressGraphWindow(QMainWindow):
    def __init__(self, profile_name, *args, **kwargs):
        super(ProgressGraphWindow, self).__init__(*args, **kwargs)

        self.profile_name = profile_name

        pg.setConfigOptions(antialias=True)

        # Pull Graph Data from .csv
        self.dates_and_weights = self.get_initial_data() # [[dates], [weights]]

        # Set Up Window Title, Size, and Style (Dark)
        self.setWindowTitle("Health History - Health Calculator")
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        # Set up Graph
        self.graphWidget = pg.PlotWidget()
        self.date_axis = pg.DateAxisItem(orientation="bottom")
        self.graphWidget.setAxisItems({'bottom':self.date_axis})

        self.graphWidget.setLabel('left', 'Weight (lb)')
        self.graphWidget.setLabel('bottom', 'Date')
        self.graphWidget.setTitle('Weight Progress Over Time')
        self.graphWidget.showGrid(x=True, y=True)
        
        self.setCentralWidget(self.graphWidget)

        self.plot_data()

    def get_initial_data(self):

        dates_and_weights = [[], []]
 
        with open("profiles.csv", 'r', newline='') as profile: 
            csv_reader = csv.reader(profile)
        
            for row in csv_reader:
                if row[0] == self.profile_name: 
                    column = 7 # Where data entries begin
                    while column < len(row):
                        current_cell_data = row[column].split(".") # Date.Weight Format
                        # The following line converts as follows: String from .csv -> datetime.datetime -> Unix timestamp
                        dates_and_weights[0].append(time.mktime((datetime.datetime.strptime(current_cell_data[0], "%m/%d/%Y").timetuple())))
                        dates_and_weights[1].append(int(current_cell_data[1]))
                        column += 1

        return dates_and_weights

    def plot_data(self):
        
        x = self.dates_and_weights[0] 
        y = self.dates_and_weights[1]
        
        plot_item = pg.PlotDataItem(x=x, y=y, size=5, pen=pg.mkPen())
        plot_item.setSymbol('x') 
        self.graphWidget.addItem(plot_item)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressGraphWindow("Chris")        
    window.show()
    app.exec() 
