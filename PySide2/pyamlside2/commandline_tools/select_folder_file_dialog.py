#!/bin/python3
# ===========================
# Ar-Ray-code 2022
# ===========================

from PySide2.QtWidgets import QApplication, QWidget, QFileDialog
import sys
import argparse

class QuestionWidget(QWidget):
    def __init__(self):
        super().__init__()

        parser = argparse.ArgumentParser(description='Select folder')
        parser.add_argument('-p', '--path', help='entry point folder')
        parser.add_argument('-f', '--file', help='Using file dialog.', action='store_true')
        parser.add_argument('-t', '--title', help='title of dialog', default='Select folder or file')
        parser.add_argument('-e', '--ext', help="file extensions (input example : '*.jpg *.png')", default='*')
        args = parser.parse_args()

        self.file_flag = args.file
        self.path = args.path
        self.title = args.title
        self.extensions = args.ext

        self.create_widgets()

    def create_widgets(self):
        if(self.file_flag==True):
            selected_usb_device = QFileDialog.getOpenFileName(self, self.title, self.path, self.extensions)[0]
        else:
            selected_usb_device = QFileDialog.getExistingDirectory(self, self.title, self.path)

        print(selected_usb_device)
        sys.exit(0)

def entry_point():
    app = QApplication(sys.argv)
    ex = QuestionWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QuestionWidget()