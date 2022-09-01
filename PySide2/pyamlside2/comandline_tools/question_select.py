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
        parser.add_argument('-al', '--answer-list', help='list of answers', nargs='+', default=['Connect', 'Abort'])
        
        args = parser.parse_args()

        self.title = args.title
        self.answer_list = args.answer_list

        self.create_widgets()

    def create_widgets(self):
        msgBox = QMessageBox()
        msgBox.setText(self.title)

        ans_get = []
        for ans in self.answer_list:
            ans_get.append(msgBox.addButton(ans, QMessageBox.ActionRole))

        msgBox.exec_()

        for ans in ans_get:
            if msgBox.clickedButton() == ans:
                print(ans.text())
                sys.exit(0)

        sys.exit(1)        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QuestionWidget()