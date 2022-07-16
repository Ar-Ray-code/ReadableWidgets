import sys
import os
import yaml
import re
import urllib.request

from .drawio_parse.parse import xml2yaml
from .utils.get_yaml import get_yaml

DEBUG_FLAG = True

LEFT = 0
CENTER = 1
RIGHT = 2

class widget_configure:
    def __init__(self):
        self.x_center = 0
        self.y_center = 0
        self.x_left = 0
        self.x_right = 0
        self.y_top = 0
        self.width = 50
        self.height = 50
        self.text = ""
        self.items = []
        self.max = 100
        self.min = 0
        self.step = 1
        self.default = 0
        self.stylesheet_str = ""
        self.font = "Arial"
        self.font_size = 10


class label_configure(widget_configure):
    def is_url(self, path: str) -> bool:
        pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if re.match(pattern, path):
            return True
        else:
            return False

    def __init__(self, yaml_abs_path: str, target_key: str) -> None:
        super().__init__()
        self.stylesheet_str = str()
        self.yaml_abs_path_file = yaml_abs_path
        self.target_key = target_key

        self.position = LEFT

        self.debug = DEBUG_FLAG


        self.yaml_data = get_yaml(self.yaml_abs_path_file)

        # exit when no yaml data
        if self.yaml_data is None:
            print("no yaml data")
            sys.exit()
        self.yaml_data = self.yaml_data[self.target_key]

    # include yaml from yaml ---------------------------------------------------
        if "include" in self.yaml_data:
            path = self.yaml_data["include"]["path"]
            key = self.yaml_data["include"]["key"]
            # is url or path
            if self.is_url(path):
                # is url -> save to ~/.cache/pyamlside2/yaml/***.yaml and load it
                # exists ~/.cache/pyamlside2/yaml/***.yaml ?
                if not os.path.exists(os.path.expanduser("~/.cache/pyamlside2/yaml/" + os.path.basename(path))):
                    os.makedirs(os.path.expanduser(
                        "~/.cache/pyamlside2/yaml"), exist_ok=True)
                    urllib.request.urlretrieve(path, os.path.expanduser(
                        "~/.cache/pyamlside2/yaml/") + os.path.basename(path))
                    print("download yaml file: " + path)
                else:
                    print("yaml file is already downloaded (Please delete ~/.cache/pyamlside2/yaml/" +
                          os.path.basename(path) + " to download again)")
                path = os.path.expanduser(
                    "~/.cache/pyamlside2/yaml/") + os.path.basename(path)

            with open(path, 'r') as f:
                self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            self.yaml_data = label_configure(path, key).yaml_data
            print("yaml_data: " + str(self.yaml_data))
            # return force
            return

    # Using common tag --------------------------------------------------------

        if "type" in self.yaml_data:
            self.type = self.yaml_data["type"]
        else:
            print("type is undefined.")
            sys.exit()

        # switching position 1 ------------------
        if "x_center" in self.yaml_data:
            self.position = CENTER
            self.x_center = int(self.yaml_data["x_center"])
        if "y_center" in self.yaml_data:
            self.y_center = int(self.yaml_data["y_center"])
        # switching position 2 ------------------
        if "x_left" in self.yaml_data:
            self.position = LEFT
            self.x_left = int(self.yaml_data["x_left"])
        # switching position 3 ------------------
        if "x_right" in self.yaml_data:
            self.position = RIGHT
            self.x_right = int(self.yaml_data["x_right"])

        if "y_top" in self.yaml_data:
            self.y_top = int(self.yaml_data["y_top"])

        if "width" in self.yaml_data:
            self.width = int(self.yaml_data["width"])

        if "height" in self.yaml_data:
            self.height = int(self.yaml_data["height"])

        if "text" in self.yaml_data:
            self.text = self.yaml_data["text"]

        if "items" in self.yaml_data:
            self.items = self.yaml_data["items"]

        if "max" in self.yaml_data:
            self.max = int(self.yaml_data["max"])

        if "min" in self.yaml_data:
            self.min = int(self.yaml_data["min"])

        if "step" in self.yaml_data:
            self.step = int(self.yaml_data["step"])

        if "default" in self.yaml_data:
            self.default = int(self.yaml_data["default"])

        if "style" in self.yaml_data:
            if "font" in self.yaml_data["style"]:
                font_list = self.yaml_data["style"]["font"].split(" ")

                for fl_s in font_list:
                    if fl_s.endswith("px") :
                        self.font_size = int(fl_s.replace("px", ""))

            if "font-family" in self.yaml_data["style"]:
                self.font = self.yaml_data["style"]["font-family"]

    # StyleSheet ---------------------------------------------------------------
        if "style" in self.yaml_data:
            # if include key
            if "include" in self.yaml_data["style"]:
                path = self.yaml_data["style"]["include"]["path"]
                key = self.yaml_data["style"]["include"]["key"]
                # is url or path
                print("path: " + path)
                if self.is_url(path):
                    # is url -> save to ~/.cache/pyamlside2/yaml/***.yaml and load it
                    # exists ~/.cache/pyamlside2/yaml/***.yaml ?
                    if not os.path.exists(os.path.expanduser("~/.cache/pyamlside2/yaml/" + os.path.basename(path))):
                        os.makedirs(os.path.expanduser(
                            "~/.cache/pyamlside2/yaml"), exist_ok=True)
                        urllib.request.urlretrieve(path, os.path.expanduser(
                            "~/.cache/pyamlside2/yaml/") + os.path.basename(path))
                        print("download yaml file: " + path)
                    else:
                        print("yaml file is already downloaded (Please delete ~/.cache/pyamlside2/yaml/" +
                              os.path.basename(path) + " to download again)")
                    print("yaml_data: " + str(self.yaml_data))
                    path = os.path.expanduser(
                        "~/.cache/pyamlside2/yaml/") + os.path.basename(path)

                with open(path, 'r') as f:
                    self.stylesheet_str = yaml.load(f, Loader=yaml.FullLoader)
                self.stylesheet_str = label_configure(
                    path, key).stylesheet_str
                # print("stylesheet_str: " + str(self.stylesheet_str))

            else:
                for key, value in self.yaml_data["style"].items():
                    # configure stylesheet
                    if (key == "background-image"):
                        # check path "./" or "../" ... (relative path)
                        # image_path : url(./image/back-image.png) -> ./image/back-image.png
                        image_path = value.replace("url(", "").replace(")", "")
                        if (image_path[0] == "." or image_path[0] == ".."):
                            basepath = os.path.dirname(self.yaml_abs_path_file)
                            image_path = os.path.join(basepath, image_path)
                            print("------------------")
                            print("image_path: " + image_path)
                            print("------------------")
                        self.stylesheet_str += key + \
                            ": url(" + image_path + ");"
                    else:
                        self.stylesheet_str += key + ": " + str(value) + "; "
            # print(self.stylesheet_str)

    # Label Rect ---------------------------------------------------------------
        if "rect" in self.yaml_data:
            if "include" in self.yaml_data["rect"]:
                path = self.yaml_data["rect"]["include"]["path"]
                key = self.yaml_data["rect"]["include"]["key"]
                if self.is_url(path):
                    # is url -> save to ~/.cache/pyamlside2/yaml/***.yaml and load it
                    # exists ~/.cache/pyamlside2/yaml/***.yaml ?
                    if not os.path.exists(os.path.expanduser("~/.cache/pyamlside2/yaml/" + os.path.basename(path))):
                        os.makedirs(os.path.expanduser(
                            "~/.cache/pyamlside2/yaml"), exist_ok=True)
                        urllib.request.urlretrieve(path, os.path.expanduser(
                            "~/.cache/pyamlside2/yaml/") + os.path.basename(path))
                        print("download yaml file: " + path)
                    else:
                        print("yaml file is already downloaded (Please delete ~/.cache/pyamlside2/yaml/" +
                              os.path.basename(path) + " to download again)")
                    path = os.path.expanduser(
                        "~/.cache/pyamlside2/yaml/") + os.path.basename(path)

                with open(path, 'r') as f:
                    self.rect_width = yaml.load(f, Loader=yaml.FullLoader)
                self.rect_width = label_configure(path, key).rect_width
                self.rect_height = label_configure(path, key).rect_height
            else:
                self.rect_width = self.yaml_data["rect"]["width"]
                self.rect_height = self.yaml_data["rect"]["height"]
        else:
            pass
            self.rect_width = self.width
            self.rect_height = self.height

        self.width = self.rect_width
        self.height = self.rect_height

    # debug ---------------------------------------------------------------
        # if "debug" in self.yaml_data:
        #     self.debug = self.yaml_data["debug"]
        # else:
        #     self.debug = False

        if self.position == LEFT:
            self.x = self.x_left
            self.y = self.y_top
        elif self.position == CENTER:
            self.x = self.x_center - self.width // 2
            self.y = self.y_center - self.height // 2
        elif self.position == RIGHT:
            self.x = self.x_right - self.width
            self.y = self.y_top - self.height
