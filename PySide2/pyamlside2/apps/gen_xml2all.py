import os
import argparse

from pyamlside2.drawio_parse.parse import xml2yaml
from pyamlside2.apps.gen_yaml2py import generate_yaml2py

def entry_point():
    parser = argparse.ArgumentParser(description="Generate template.")
    parser.add_argument("--input", "-i", help="input xml file", required=True)
    parser.add_argument("--output-dir", "-o", help="output directory", required=True)
    args = parser.parse_args()

    print("================== rw_gen_xml2all ======================")
    print("input: " + args.input)
    print("output-dir: " + args.output_dir)
    print("=========================================================")

    os.makedirs(args.output_dir, exist_ok=True)
    intput_basename_no_exps = os.path.basename(args.input).split(".")[0]

    # generate yaml
    yaml_str = xml2yaml(args.input)
    with open(args.output_dir + "/" + intput_basename_no_exps + ".yaml", "w") as f:
        f.write(yaml_str)

    # generate py
    gen_py = generate_yaml2py()
    str_python = gen_py.generate_py(args.output_dir + "/" + intput_basename_no_exps + ".yaml")
    with open(args.output_dir + "/" + intput_basename_no_exps + ".py", "w") as f:
        f.write(str_python)

    print("Generate template done.")
    print("run `$ python3 " + args.output_dir + "/" + intput_basename_no_exps + ".py " + args.output_dir + "/" + intput_basename_no_exps + ".yaml`")

if __name__ == '__main__':
    entry_point()
