# before doing that change version number in setup.py

# removing dist and build

rm -rf dist build

# building again

python setup.py bdist_wheel sdist

# now upload new version to pypi.org

twine upload dist/*