from pyamlside2.drawio_parse.parse import xml2yaml
import argparse

def parse():
    args = argparse.ArgumentParser()
    args.add_argument("-i", "--input", help="input xml file", required=True)
    args.add_argument("-o", "--output", help="output yaml file", required=True)

    yaml_str = xml2yaml(args.parse_args().input)
    with open(args.parse_args().output, "w") as f:
        f.write(yaml_str)
    print("Done.")

if __name__ == "__main__":
    parse()