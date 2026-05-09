#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

echo "🧹 Cleaning up old builds..."
rm -rf dist/ build/ src/*.egg-info

echo "📦 Installing publish dependencies..."
python -m pip install build twine

echo "🏗️ Building package..."
python -m build

echo "🔍 Checking distribution..."
python -m twine check dist/*

echo "🚀 Uploading to PyPI..."
echo "(You can use '__token__' as username and your PyPI token as password)"
python -m twine upload dist/*

echo "✅ Done!"
