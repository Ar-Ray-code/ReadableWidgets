import sys
import os

from pyamlside2.mainwindow import PyamlSide2Window
from PySide2.QtWidgets import QApplication

class MainWindow(PyamlSide2Window):
    def __init__(self):
        yaml_path = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")
        super().__init__(yaml_path)
        self.show()

def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    entry_point()