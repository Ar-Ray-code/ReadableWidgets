
import sys

from pyamlside2.mainwindow import PyamlSide2Window
from PySide2.QtWidgets import QApplication

class MainWindow(PyamlSide2Window):
    def __init__(self, args):
        self.number = 0
        if (len(args) == 2):
            super().__init__(args[1])
        else:
            print("No args.")
            exit(1)

        self.widgets["start_stop_button"].clicked.connect(self.start_stop_button_update)
        self.widgets["exit_button"].clicked.connect(self.exit_button_update)
        self.widgets["spinbox"].valueChanged.connect(self.spinbox_update)
        self.widgets["combobox"].currentIndexChanged.connect(self.combobox_update)
        self.widgets["lineedit"].textChanged.connect(self.lineedit_update)
        self.widgets["slider1"].valueChanged.connect(self.slider1_update)
        self.widgets["slider2"].valueChanged.connect(self.slider2_update)
        self.widgets["checkbox"].stateChanged.connect(self.checkbox_update)
        self.widgets["progressbar"].valueChanged.connect(self.progressbar_update)

        self.show()

    def start_stop_button_update(self):
        print("start_stop_button clicked.")

    def exit_button_update(self):
        print("exit_button clicked.")

    def spinbox_update(self):
        print("spinbox clicked.")
        print("spinbox value: ", self.widgets["spinbox"].value())

    def combobox_update(self):
        print("combobox clicked.")
        print("combobox value: ", self.widgets["combobox"].currentText())

    def lineedit_update(self):
        print("lineedit clicked.")
        print("lineedit value: ", self.widgets["lineedit"].text())

    def slider1_update(self):
        print("slider1 clicked.")
        print("slider1 value: ", self.widgets["slider1"].value())

    def slider2_update(self):
        print("slider2 clicked.")
        print("slider2 value: ", self.widgets["slider2"].value())

    def checkbox_update(self):
        print("checkbox clicked.")
        print("checkbox value: ", self.widgets["checkbox"].isChecked())

    def progressbar_update(self):
        print("progressbar clicked.")
        print("progressbar value: ", self.widgets["progressbar"].value())


def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    entry_point()
