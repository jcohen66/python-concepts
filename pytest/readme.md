# Must run from module.

## Run Tests
python -m pytest
python -m pytest -vv
python -m pytest --lf

### Run single test
python -m pytest ./tests/test_project_module.py::test_rolling_average
