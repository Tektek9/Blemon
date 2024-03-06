import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox
from PyQt5.QtGui import QColor
import pyqtgraph as pg
import serial

#Suimpel Monitoring BLE ESP32 ke Desktop
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BLE Monitoring")
        self.central_widget = QVBoxLayout()
        self.graphWidget = pg.PlotWidget()
        self.central_widget.addWidget(self.graphWidget)
        self.devCombo = QComboBox()
        self.devCombo.currentIndexChanged.connect(self.updateGraph)
        self.central_widget.addWidget(self.devCombo)
        self.setCentralWidget(self.graphWidget)
        self.sPort = serial.Serial('/dev/ttyUSB0', 115200)
        self.x = {}
        self.y = {}
        self.warna = [QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255)]
        self.garis_data = {}

    def updateGraph(self):
        data = self.sPort.readline().decode('utf-8').strip()
        mac, nama, rssi = data.split(':')
        rssi = int(rssi)
        if mac not in self.x:
            self.x[mac] = []
            self.y[mac] = []
            self.garis_data[mac] = self.graphWidget.plot(pen=self.warna[len(self.x) % len(self.warna)])

        self.x[mac].append(len(self.x[mac]))
        self.y[mac].append(rssi)
        self.garis_data[mac].setData(self.x[mac], self.y[mac])

        if nama not in [self.devCombo.itemText(i) for i in range(self.devCombo.count())]:
            self.devCombo.addItem(nama)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    simpelMon = Main()
    simpelMon.show()
    sys.exit(app.exec_())