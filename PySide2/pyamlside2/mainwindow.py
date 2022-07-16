import time
import yaml
import os

from pyamlside2.create_widgets import create_widgets
from PySide2.QtWidgets import QMainWindow

from .drawio_parse.parse import xml2yaml
from .utils.get_yaml import get_yaml


class PyamlSide2Window(QMainWindow):
    def __init__(self, yaml_path: str = None):
        self.yaml_abs_path = os.path.abspath(yaml_path)
        self.number = 0
        self.time_val = int(time.time())
        self.start_flag = False

        super().__init__()

        if yaml_path != None:
            self.init_window()
            self.create_widgets()

        # geometry setting ---
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

    def __del__(self):
        pass

    def create_widgets(self):
        # Template ---
        self.widgets, self.stylesheet = self.create_all_widgets()
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ------------

    def init_window(self):
        yaml_data = get_yaml(self.yaml_abs_path)
        window_data = yaml_data["WINDOW"]

        if "width" in window_data:
            self.width = window_data["width"]
            self.height = window_data["height"]
            self.title = window_data["title"]
        else:
            self.width = window_data["rect"]["width"]
            self.height = window_data["rect"]["height"]
            self.title = window_data["text"]

        if "x" in window_data:
            self.x = window_data["x"]
            self.y = window_data["y"]
        elif "x_left" in window_data:
            self.x = window_data["x_left"]
            self.y = window_data["y_top"]

# Template ================================================================
    def create_all_widgets(self) -> dict:
        widgets, stylesheet_str = dict(), dict()
        self.yaml_data = get_yaml(self.yaml_abs_path)


        for key in self.yaml_data:
            data = create_widgets.create(self, self.yaml_abs_path, key)
            widgets[key], stylesheet_str[key] = data[0], data[1]

        return widgets, stylesheet_str
# =========================================================================
