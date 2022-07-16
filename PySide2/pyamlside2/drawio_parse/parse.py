# from types import NoneType
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, tostring
from .propaties_class import object_propaties

no_name_count = 0
log = False

def attrib_parse(input_element: Element) -> object_propaties:
    global no_name_count

    widget = object_propaties()
    if input_element is None:
        return None

    mygeometry_found = False
    for child in input_element:
        if child.attrib['as'] == 'geometry':
            if 'x' in child.attrib:
                widget.rect.x_left = int(child.attrib['x'])
            else:
                widget.rect.x_left = 0

            if 'y' in child.attrib:
                widget.rect.y_top = int(child.attrib['y'])
            else:
                widget.rect.y_top = 0

            if 'width' in child.attrib:
                widget.rect.width = int(child.attrib['width'])
            else:
                widget.rect.width = 0

            if 'height' in child.attrib:
                widget.rect.height = int(child.attrib['height'])
            else:
                widget.rect.height = 0

            mygeometry_found = True

    if not mygeometry_found:
        return None
    # --------------------------------------------------------------------------------------------------------------------
    text = input_element.attrib['value']
    style_text = input_element.attrib['style']

    if text.find("<b>") != -1:
        widget.style.bold = True
        text = text.replace("<b>", "")
        text = text.replace("</b>", "")
    if text.find("<i>") != -1:
        widget.style.italic = True
        text = text.replace("<i>", "")
        text = text.replace("</i>", "")

    # analyze text for style
    if text.find("<font") != -1:
        if text.find("face=\"") != -1:
            font_family = text.split("face=\"")[1].split("\"")[0]
            widget.style.font_family = font_family
        # style="font-size: 14px; color="#0066cc"
        if text.find("font-size:") != -1:
            font_size = text.split("font-size: ")[1].split("px;")[0]
            widget.style.font_size = font_size + "px"
        # color -> text_color
        if text.find("color=\"") != -1:
            text_color = text.split("color=\"")[1].split("\"")[0]
            widget.style.text_color = text_color

        text = text.split(">")[1].split("</font")[0]

    if style_text.find("fillColor") != -1:
        widget.style.background_color = style_text.split("fillColor=")[1].split(";")[0]
        if widget.style.background_color == "none":
            widget.style.background_color = "None"
    if style_text.find("strokeColor") != -1:
        widget.style.border_color = style_text.split("strokeColor=")[1].split(";")[0]
        if widget.style.border_color == "none":
            widget.style.border_color = "None"

    widget.widget_type = "q" + text.split(":")[0]
    widget.widget_id = text.split(":")[1]
    widget.text = text.split(":")[1]

    if log:
        print("----------------------------------------------------")
        print("widget_id: " + widget.widget_id)
        print("widget_type: " + widget.widget_type)
        print("rect: " + str(widget.rect.x_left) + " " + str(widget.rect.y_top) + " " + str(widget.rect.width) + " " + str(widget.rect.height))

        print("bold: " + str(widget.style.bold))
        print("italic: " + str(widget.style.italic))
        print("font_size: " + widget.style.font_size)
        print("font_family: " + widget.style.font_family)
        print("text_color: " + widget.style.text_color)
        print("background_color: " + widget.style.background_color)
        print("border_color: " + widget.style.border_color)

    return widget

def generate_yaml(_widget: object_propaties) -> str:
    if _widget is None:
        return ""

    _yaml_text = ""
    _tab_length = 2
    _tab = ""
    _n = "\n"
    for i in range(_tab_length):
        _tab += " "

    _ntab = _n + _tab
    _dtab = _tab + _tab
    _ndtab = _n + _dtab

    _yaml_text += _widget.widget_id + ":"
    _yaml_text += _ntab + "type: " + _widget.widget_type
    _yaml_text += _ntab + "x_left: " + str(_widget.rect.x_left)
    _yaml_text += _ntab + "y_top: " + str(_widget.rect.y_top)
    _yaml_text += _ntab + "rect:"
    _yaml_text += _ndtab + "width: " + str(_widget.rect.width)
    _yaml_text += _ndtab + "height: " + str(_widget.rect.height)

    _yaml_text += _ntab + "text: " + _widget.text
    _yaml_text += _ntab + "style:"

    _font_text = "font: "
    if _widget.style.bold:
        _font_text += "bold "
    if _widget.style.italic:
        _font_text += "italic "
    _font_text += _widget.style.font_size

    _yaml_text += _ndtab + _font_text
    if _widget.style.text_color is not None:
        _yaml_text += _ndtab + "color: '" + _widget.style.text_color + "'"
    if _widget.style.background_color != "None":
        _yaml_text += _ndtab + "background-color: '" + _widget.style.background_color + "'"
    _yaml_text += _ndtab + "font-family: " + _widget.style.font_family

    return _yaml_text + _n

def xml2yaml(xmlfile: str) -> str:
    tree = ElementTree.parse(xmlfile)

    title_added = False
    title = object_propaties()

    widgets = []
    elem = tree.getroot()
    # next
    for child in elem:
        for child2 in child:
            if title_added == False:
                title.rect.x_left = 0
                title.rect.y_top = 0
                title.rect.width = child2.attrib["dx"]
                title.rect.height = child2.attrib["dy"]

                title.widget_type = "window"
                title.widget_id = "WINDOW"
                title.text = xmlfile.split('/')[-1].split('.')[0]

                widgets.append(title)
                title_added = True

            for child3 in child2:
                #mxGraphModel
                for child4 in child3:
                    widgets.append(attrib_parse(child4))

    txt = ""
    for _widget in widgets:
        txt += generate_yaml(_widget)

    return txt

    # print(txt)


if __name__ == '__main__':
    # XML ファイルから ElementTree オブジェクトを生成
    xmlfile = '../drawio_xml/example_gui.xml'
    xml2yaml(xmlfile)
    print("done")
