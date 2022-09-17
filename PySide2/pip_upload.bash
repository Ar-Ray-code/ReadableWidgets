python -m pip install wheel twine
rm -f -r *.egg-info/* dist/*
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*