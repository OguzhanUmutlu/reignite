#!/usr/bin/env bash

set -e
cd "$(dirname "$0")"
bash run_tests.sh
rm -rf dist/ build/ src/*.egg-info
python -m pip install build twine
python -m build
python -m twine check dist/*
echo "(You can use '__token__' as username and your PyPI token as password)"
python -m twine upload dist/*
