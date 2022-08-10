pip3 install wheel twine
rm -f -r *.egg-info/* dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*