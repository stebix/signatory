.PHONY: genreadme setup test docs
.RECIPEPREFIX+=

# generate the readme from the documentation
genreadme:
    python genreadme.py

# run setup.py
setup:
    python setup.py $@

# run tests
test:
    python -m test.runner

# make docs
docs:
    sphinx-build -M html ./docs ./docs/_build