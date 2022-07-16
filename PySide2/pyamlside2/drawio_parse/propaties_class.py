
class style:
    def __init__(self):
        self.background_color = '#FFFFFF'
        self.text_color = '#000000'
        self.border_color = '#000000'
        self.font_size = '12' + 'px'
        self.font_family = 'Arial'
        self.bold = False
        self.italic = False

class rect:
    def __init__(self):
        self.x_left = 0
        self.y_top = 0
        self.width = 0
        self.height = 0

class object_propaties:
    def __init__(self):
        self.widget_id = ""
        self.widget_type = ""
        self.text = ""
        self.style = style()
        self.rect = rect()