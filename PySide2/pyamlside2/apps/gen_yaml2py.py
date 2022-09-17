import sys
import os
from pyamlside2.label_configure import label_configure
from pyamlside2.utils.get_yaml import get_yaml

import argparse

class generate_yaml2py():
    def __init__(self):
        self.tab = "    "
        self.tab2 = "        "

        self.widgets_keyword = {
            "qpushbutton": "clicked",
            "qlineedit": "textChanged",
            "qcheckbox": "stateChanged",
            "qcombobox": "currentIndexChanged",
            "qspinbox": "valueChanged",
            "qslider": "valueChanged",
            "qprogressbar": "valueChanged",
        }

# Header - Middle - Footer ===================================
        self.header ="""
import sys

from pyamlside2.mainwindow import PyamlSide2Window
from PySide2.QtWidgets import QApplication

class MainWindow(PyamlSide2Window):
    def __init__(self, args):
        if (len(args) == 2):
            super().__init__(args[1])
        else:
            print("No args.")
            exit(1)

"""

        self.middle ="""
        self.show()

"""

        self.footer ="""
def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    entry_point()
"""
# =============================================================

    def generate_py(self, input_yaml_path:str) -> str:
        yaml_abs_path = os.path.abspath(input_yaml_path)

        # add definition
        export_py_str = self.header
        yaml_data = get_yaml(yaml_abs_path)
        for key in yaml_data:
            config = label_configure(yaml_abs_path, key)
            # add function
            for widget_key in self.widgets_keyword:
                if widget_key in config.type:
                    export_py_str += self.tab2 + "self.widgets[\"" + key + "\"]." + self.widgets_keyword[widget_key] + ".connect(self." + key + "_update" + ")\n"

        export_py_str += self.middle

        for key in yaml_data:
            config = label_configure(yaml_abs_path, key)
            # add function
            for widget_key in self.widgets_keyword:
                if widget_key in config.type:
                    export_py_str += self.tab + "def " + key + "_update(self):\n"
                    export_py_str += self.tab2 + "print(\"" + key + " clicked.\")\n"
                    # print slider value
                    if widget_key == "qslider":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].value())\n"
                    # print combobox value
                    if widget_key == "qcombobox":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].currentText())\n"
                    # print checkbox value
                    if widget_key == "qcheckbox":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].isChecked())\n"
                    # print lineedit value
                    if widget_key == "qlineedit":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].text())\n"
                    # print spinbox value
                    if widget_key == "qspinbox":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].value())\n"
                    # print progressbar value
                    if widget_key == "qprogressbar":
                        export_py_str += self.tab2 + "print(\"" + key + " value: \", self.widgets[\"" + key + "\"].value())\n"

                    export_py_str += "\n"
                    break

        export_py_str += self.footer
        return export_py_str

def entry_point():
    parser = argparse.ArgumentParser(description="Generate template.")
    parser.add_argument("--input", "-i", help="input yaml file", required=True)
    parser.add_argument("--output", "-o", help="output py file", required=True)
    args = parser.parse_args()

    gen_py = generate_yaml2py()
    str_python = gen_py.generate_py(args.input)
    with open(args.output, "w") as f:
        f.write(str_python)

    print("Generate template done.")

if __name__ == '__main__':
    entry_point()
