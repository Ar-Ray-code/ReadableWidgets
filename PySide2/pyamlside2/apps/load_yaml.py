import sys
import os

from pyamlside2.mainwindow import PyamlSide2Window
from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets

class MainWindow(PyamlSide2Window):
    def __init__(self, args):
        self.number = 0
        if (len(args) == 2):
            super().__init__(args[1])
        else:
            print("No args.")
            super().__init__("../PySide2/yaml/header.yaml")

        menuList = QtWidgets.QMenu(self)
        # add menubar
        action1 = QtWidgets.QAction("reload", self)
        action1.triggered.connect(self.reload)

        action2 = QtWidgets.QAction("select file", self)
        action2.triggered.connect(self.select_file)

        menuList.addAction(action1)
        menuList.addAction(action2)

        menu_button = QtWidgets.QPushButton("Menu", self)
        menu_button.setMenu(menuList)

        self.show()

    def reload(self):
        os.execv(sys.argv[0], sys.argv)

    def select_file(self):
        # widget
        file_dialog = QtWidgets.QFileDialog()
        # xml or yaml
        file_dialog.setNameFilters(["YAML (*.yaml)", "XML (*.xml)"])
        # open file
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        # select file
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            os.execv(sys.argv[0], [sys.argv[0], file_path])


def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow(sys.argv)
    sys.exit(app.exec_())


if __name__ == '__main__':
    entry_point()
