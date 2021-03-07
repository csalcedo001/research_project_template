#!/bin/bash

# Create folders, execute one-run files (e.g. setup python package), etc.

# Setup python package
cd package
python3 setup.py sdist bdist_wheel
pip3 install -e .
cd ..

python3 scripts/setup/setup.py
