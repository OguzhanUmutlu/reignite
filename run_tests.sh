#!/bin/bash

python codegen.py
source venv/bin/activate
python -m pip install -e ".[test]"
python -m pytest -q

