#!/bin/bash

python scripts/scrapesdf.py
source venv/bin/activate
python -m pip install -e ".[test]"
python -m pytest -q

