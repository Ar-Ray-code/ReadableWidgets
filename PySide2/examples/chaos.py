import sys
import datetime
import time
import os


from pyamlside2.mainwindow import PyamlSide2Window

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication

from pyamlside2.commandline_tools.simple_widget import *

YAML = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")

class MainWindow(PyamlSide2Window):
    def __init__(self):
        super().__init__(YAML)

        self.widgets["start_stop_button"].clicked.connect(self.button_update)

        self.widgets["exit_button"].clicked.connect(self.exit)
        self.widgets["spinbox"].valueChanged.connect(self.spinbox_update)

        self.widgets["progressbar"].setMaximum(100)
        self.widgets["progressbar"].setMinimum(0)
        self.widgets["progressbar"].setValue(50)

        self.widgets["lcd_number"].display(334)
        self.widgets["lineedit"].setText("qawsedrftgyhujikolp")

        # create timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start(10)

    def spinbox_update(self):
        self.value = self.widgets["spinbox"].value()

    def button_update(self):
        if self.start_flag == False:
            self.start_flag = True
            self.widgets["start_stop_button"].setText('Stop')
            self.widgets["start_stop_button"].setStyleSheet(self.stylesheet["stop-stylesheet"])

            self.time_val = int(time.time()) + 5
        else:
            self.start_flag = False
            self.widgets["start_stop_button"].setText('Start')
            self.widgets["start_stop_button"].setStyleSheet(self.stylesheet["start_stop_button"])

    def exit(self):
        # ask
        reply = exec_messagebox("Are you sure to quit?", "question")
        if reply =="No":
            return
        sys.exit()

    def timer_update(self):
        self.time_val = int(time.time())

        if self.start_flag == True:
            self.number += 1
            if self.number >= 100:
                self.number = 0
        else:
            pass

        self.widgets["lcd_number"].display(self.number)
        self.widgets["progressbar"].setValue(self.number)
        self.widgets["spinbox"].setValue(self.number)
        self.widgets["slider1"].setValue(self.number)
        self.widgets["slider2"].setValue(self.number)

        self.widgets["datetime_label"].setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.update()
        self.show()
        self.timer.start(10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
