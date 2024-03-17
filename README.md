# Demo Web Automation Framework

This demo project, built by me, is intended to demonstrate how a Framework using POM (Page Object Model), which, using the Selenium, Pytest, and Allure tools, allows you to connect almost any web-application to it and start testing quickly.

### Installing

Just download this project to Python virtual environment on your local computer and install dependencies using file requirements.txt:

pip3 -r requirements.txt

You must install Java on your local machine to use Allure for the test reports.

Also, please set the path for your drivers in the file webdriverfactory.py, located ../demoWebAutomationFramework/base/ 

### Running the tests

Use this command in the terminal from your virtual environment to run Demo Test Suite:

py.test tests/test_suite_demo.py 

or that for using chrome driver

py.test tests/test_suite_demo.py --browser chrome


### Getting the Allure reports

Use this command in the terminal from your virtual environment if you want to get the Allure report:

1. py.test tests/test_suite_demo.py --alluredir=allureress 

2. (Path to your project directory)../demoWebAutomationFramework/allure-2.10.0/bin/allure serve allureress


### For use with other projects

Set project URL in the “baseURL” variable in the file webdriverfactory.py, located ../ demoWebAutomationFramework/base/

Using the Page Object Model, create Page and Test classes in packages located ../ demoWebAutomationFramework/page/ 

and 

../ demoWebAutomationFramework/tests/

respectively.

