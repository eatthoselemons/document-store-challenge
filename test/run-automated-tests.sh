source ../venv/bin/activate

cd automated
python -m unittest ApiTests.BasicApiTests
python -m unittest FileApiTests.FileApiTests
