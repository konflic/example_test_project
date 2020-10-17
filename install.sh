#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip isntall -U pip
pip install -Ur requirements.txt
