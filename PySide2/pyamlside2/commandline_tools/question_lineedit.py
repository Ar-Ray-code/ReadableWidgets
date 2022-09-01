#!/bin/python3
# ===========================
# Ar-Ray-code 2022
# ===========================

from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog
import sys
import argparse

class QuestionWidget(QWidget):
    def __init__(self):
        super().__init__()

        parser = argparse.ArgumentParser(description='Select folder')
        parser.add_argument('-t', '--title', help='title of dialog', default='Choose your answer')
        parser.add_argument('-d', '--default', help='default answer', default='')

        args = parser.parse_args()

        self.title = args.title
        self.default = args.default

        self.create_widgets()

    def create_widgets(self):
        lineEdit = QInputDialog()
        lineEdit.setLabelText(self.title)

        ans, _ = lineEdit.getText(self, self.title, self.title, QLineEdit.Normal, self.default)
        print(ans)
        sys.exit(0)

def entry_point():
    app = QApplication(sys.argv)
    ex = QuestionWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QuestionWidget()