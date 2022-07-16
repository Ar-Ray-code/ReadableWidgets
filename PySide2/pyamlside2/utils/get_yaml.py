import yaml
from ..drawio_parse.parse import xml2yaml

def get_yaml(any: str) -> str:
    if any.endswith(".xml"):
        yaml_text = xml2yaml(any)
        yaml_data = yaml.load(yaml_text, Loader=yaml.FullLoader)
    else:
        with open(any, 'r') as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)

    return yaml_data