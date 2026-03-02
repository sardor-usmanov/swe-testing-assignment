# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a minimal calculator application that supports addition, subtraction, multiplication, division (with graceful handling of division by zero), and a Clear (C) action that resets the current result to zero. The project is intentionally simple in UI to emphasize clean, testable code, version control discipline, and a multi-layered testing strategy (unit + integration).

## Features
- Addition, subtraction, multiplication, division
- Graceful division-by-zero handling
- Clear (C) resets display to `0`
- Unit and integration test suite using `pytest`

## Tech Stack
- Python 3
- pytest (testing)

## Project Structure
```text
swe-testing-assignment/
  src/
    calculator.py
    app.py
  tests/
    unit/
      test_calculator.py
    integration/
      test_app_flow.py
  pytest.ini
  requirements.txt
  README.md
  TESTING.md