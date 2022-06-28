
# A Python based simple calculator

A Python based simple calculator, outlining project structure & unit tests
## Authors

- [@Adarsh Battu](https://github.com/adarshbattu109/adarshbattu109)


## Installation

Create a Virtual Environment

```bash
  # Install the virtualenv module
  pip install virtualenv

  # Create the virtual Environment named .venv
  python -m venv .venv

  # Activate the Virtual Environment
  .venv\Scripts\activate
```
    
Install the Application

```bash
  # Install the simple calculator app
  pip install -e .
```


## Running Tests

To run the tests, refer the following

 - Flake8
  ```bash
  flake8 src test --ignore=E501
  ```
 - Pytest
  ```bash
  pytest -v
  ```
 - mypy
  ```bash
  mypy src test
  ```