#!/bin/bash

# Create folders, execute one-run files (e.g. setup python package), etc.
mkdir -p runs

# Setup python package
cd package

cp ../README.md .

python3 setup.py sdist bdist_wheel
pip3 install -e .

rm README.md

cd ..

python3 scripts/setup/setup.py
