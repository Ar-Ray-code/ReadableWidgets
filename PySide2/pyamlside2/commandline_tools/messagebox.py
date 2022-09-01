#!/bin/python3
# ===========================
# Ar-Ray-code 2022
# ===========================

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import argparse

class QuestionWidget(QWidget):
    def __init__(self):
        super().__init__()

        parser = argparse.ArgumentParser(description='Select folder')
        parser.add_argument('-t', '--title', help='title of dialog', default='Choose your answer')
        parser.add_argument('-ty', '--type', help='type of dialog', default='question')
        
        args = parser.parse_args()

        self.title = args.title
        self.type = args.type

        self.create_widgets()

    def create_widgets(self):

        # switch case
        if self.type == 'information':
            msgBox = QMessageBox.information(self, self.title, self.title)
        elif self.type == 'question':
            msgBox = QMessageBox.question(self, self.title, self.title)
            if msgBox == QMessageBox.Yes:
                print('Yes')
            elif msgBox == QMessageBox.No:
                print('No')
        elif self.type == 'warning':
            msgBox = QMessageBox.warning(self, self.title, self.title)
        elif self.type == 'critical':
            msgBox = QMessageBox.critical(self, self.title, self.title)
        else:
            exit(1)

def entry_point():
    app = QApplication(sys.argv)
    ex = QuestionWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QuestionWidget()