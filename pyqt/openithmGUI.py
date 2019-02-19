from __future__ import division, unicode_literals, with_statement

import sys, serial, time, atexit
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QThread, QTimer
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow

from mainUI import Ui_MainWindow

class OpeNITHM():
    open_serial = False

    touchboard = {
        "threshold": -1,
        "deadzone": -1,
        "alpha": -1.0
    }

    ir = {
        "deadzone": -1,
        "alpha": -1.0
    }

    def __init__(self, baudrate=115200, port="COM3", timeout=1):
        self.s = serial.Serial()
        self.s.baudrate = baudrate
        self.s.port = port
        self.s.timeout = timeout
        #print(self.s.name)

    def __enter__(self):
        self.openSerial()
        return self

    def __exit__(self, type, value, traceback):
        self.closeSerial()

    def serialWrite(self, payload):
        self.s.write(payload)

    def serialRead(self, buffer=1): # reads from serial, buffer is in bytes
        return self.s.read(buffer)

    def serialReadLine(self): # reads until \n or timeout
        return self.s.readline()

    def getTouchboard(self, value):
        return self.touchboard.get(value)

    def getIR(self, value):
        return self.ir.get(value)

    def updateValues(self):
        self.serialWrite(b'g ') # request to print

        # iteratively assign each given value to dictionary until we reach a semicolon
        result = dict()
        line = ["", ""]
        while ';' not in line:
            line = self.serialReadLine().decode("ASCII").split(" \t")
            #print(line)
            if len(line) == 2:
                result[line[0].replace(";", "")] = line[1].replace("\r\n", "")

        #print(result)

        # update values in dictionary
        self.touchboard['threshold'] = int(result.get('tt')) if result.get('tt') != None else -1
        self.touchboard['deadzone']  = int(result.get('td')) if result.get('td') != None else -1
        self.touchboard['alpha']     = float(result.get('ta')) if result.get('ta') != None else -1.0
        self.ir['deadzone']          = int(result.get('id')) if result.get('id') != None else -1
        self.ir['alpha']             = float(result.get('ia')) if result.get('ia') != None else -1.0

    def setTouchboard(self, setting, val):
        payload = None
        if setting == 'threshold':
            payload = 'tt' + str(int(val))
        elif setting == 'deadzone':
            payload = 'td' + str(int(val))
        elif setting == 'alpha':
            payload = 'ta' + str(float(val))
        if payload != None:
            #print(payload)
            self.serialWrite(payload.encode('ASCII'))

    def setIR(self, setting, val):
        payload = None
        if setting == 'deadzone':
            payload = 'id' + str(int(val))
        elif setting == 'alpha':
            payload = 'ia' + str(float(val))
        if payload != None:
            #print(payload)
            self.serialWrite(payload.encode('ASCII'))

    def calibrateTouchboard(self):
        self.serialWrite(b'tc')

    def calibrateIR(self):
        self.serialWrite(b'ic')

    def pause(self):
        self.serialWrite(b'p ')
        #print("Paused.")
    
    def resume(self):
        self.serialWrite(b'r ')
        #print("Resumed.")

    def getState(self):
        if self.open_serial:
            self.serialWrite(b'a ') # request to print
            result = ""
            while ';' not in result:
                result += self.serialRead().decode("ASCII")
            #print(result)
            if int(result[0]):
                return "Running"
            else:
                return "Paused"
        else:
            return "Not Connected"

    def openSerial(self, wait=5):
        self.s.open()
        time.sleep(wait)
        self.open_serial = True
        #print("Opened serial connection.")

    def closeSerial(self):
        self.s.close()
        self.open_serial = False
        #print("Closed serial connection.")
        

class MainWindow(QMainWindow):

    def __init__(self, op):
        super(MainWindow, self).__init__()
        #uic.loadUi("openithm.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.op = op

        self.ui.tapply.clicked.connect(self.touchboardApply)
        self.ui.irapply.clicked.connect(self.irApply)
        self.ui.tcalibrate.clicked.connect(self.op.calibrateTouchboard)
        self.ui.ircalibrate.clicked.connect(self.op.calibrateIR)
        self.ui.pause.clicked.connect(self.op.pause)
        self.ui.resume.clicked.connect(self.op.resume)
        self.show()

    def updateValues(self):
        self.ui.thres_current.setText(QApplication.translate("MainWindow", "Current: " + str(self.op.getTouchboard('threshold')), None, -1))
        self.ui.dead_current.setText(QApplication.translate("MainWindow", "Current: " + str(self.op.getTouchboard('deadzone')), None, -1))
        self.ui.alpha_current.setText(QApplication.translate("MainWindow", "Current: " + str(self.op.getTouchboard('alpha')), None, -1))

        self.ui.irdead_current.setText(QApplication.translate("MainWindow", "Current: " + str(self.op.getIR('deadzone')), None, -1))
        self.ui.iralpha_current.setText(QApplication.translate("MainWindow", "Current: " + str(self.op.getIR('alpha')), None, -1))

        self.ui.status.setText(QApplication.translate("MainWindow", "Status: " + self.op.getState(), None, -1))

    def touchboardApply(self):
        self.op.setTouchboard('threshold', self.ui.thres_val.value())
        self.op.setTouchboard('deadzone', self.ui.dead_val.value())
        self.op.setTouchboard('alpha', self.ui.alpha_val.value())

    def irApply(self):
        self.op.setIR('deadzone', self.ui.irdead_val.value())
        self.op.setIR('alpha', self.ui.iralpha_val.value())

class UpdateThread(QThread):
    def __init__(self, op, window):
        super(UpdateThread, self).__init__()
        self.op = op
        self.window = window

    def run(self):
        while True:
            self.op.updateValues()
            self.window.updateValues()
            #print("Updating values...")
            time.sleep(1)

def main():
    app = QApplication(sys.argv)
    # temporary read until UI is finalized
    #f = QFile("openithm.ui")
    #f.open(QFile.ReadOnly)
    #loader = QUiLoader()
    #window = loader.load(f)
    #window.show()

    op = OpeNITHM()
    window = MainWindow(op)
    op.openSerial()

    atexit.register(op.closeSerial)

    t = UpdateThread(op, window)
    t.start()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()