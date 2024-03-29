import setuptools
import re
from os import path
import os


def get_version():
    with open("pyamlside2/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files("yaml")

readme_path = path.abspath(path.dirname(__file__))
with open(path.join(readme_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="pyamlside2",
    packages=["pyamlside2", "pyamlside2.drawio_parse", "pyamlside2.utils", "pyamlside2.apps", "pyamlside2.commandline_widgets"],
    package_data={"pyamlside2": extra_files},

    version=get_version(),
    author="Ar-Ray-code",
    author_email="ray255ar@gmail.com",

    url="https://github.com/Ar-Ray-code/ReadableWidgets",
    description="PySide2 configuration in yaml format providing the most simple script.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='PySide2 yaml',
    license="MIT",
    python_requires=">=3.8",
    install_requires=["PyYAML", "PySide2"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Source": "https://github.com/Ar-Ray-code/ReadableWidgets",
        "Tracker": "https://github.com/Ar-Ray-code/ReadableWidgets/issues",
    },
    entry_points={
        "console_scripts": [
            "rw_view_yaml2pyside2 = pyamlside2.apps.view_yaml2pyside2:entry_point",
            "rw_gen_xml2yaml = pyamlside2.apps.gen_xml2yaml:entry_point",
            "rw_gen_yaml2py = pyamlside2.apps.gen_yaml2py:entry_point",
            "rw_gen_xml2all = pyamlside2.apps.gen_xml2all:entry_point",
            "messagebox = pyamlside2.commandline_widgets.messagebox:entry_point",
            "select_folder_file_dialog = pyamlside2.commandline_widgets.select_folder_file_dialog:entry_point",
            "question_lineedit = pyamlside2.commandline_widgets.question_lineedit:entry_point",
            "question_select = pyamlside2.commandline_widgets.question_select:entry_point",
        ],
    }
)
