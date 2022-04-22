# Testing in Python: Unit Tests


This repo contains an exmaple of a unit tests in python. In this repo, I show how to run the unit tests, it achieving 100% test coverage by the full path of each methods **[Click here to see the paths and Control Flow Graphs](https://docs.google.com/document/d/1B-K0-3lXkQINmqJXbrpO1EQHXbjJUgUczpln04QyJa8/edit?usp=sharing)**

- install the dependanceies:  
```console
pip3 install -r requirements.txt 
```

# Steps 

## Run test using pytest
```console
pytest test_calculatorApp.py 
```

## Code coverage
- To display the code coverage page, open the htmlcov folder then open the index.html file on your browser.
- To create a more concise html version of the report, Run:  
 ```console 
    coverage html 
 ```

## Run the test and generate code coverage
- Run the following command to run the tests and print the code coverage:
    - 
    ```console 
    pytest --cov=calculatorApp 
    ```
- To display the report page, open the htmlcov folder then open the calculatorApp_py.html file on your browser.
- Run the following command to run the tests and generate html report for the code coverage: 
    - 
    ```console 
    pytest --cov=calculatorApp --cov-report=html 
    ```
