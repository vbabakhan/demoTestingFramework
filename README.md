# Demo Web Testing Framework by Python

This demo project is intended to demonstrate how I build a Framework using POM (Page Object Model), using the Selenium-webdriver, Pytest, and Allure tools, which allows to connect almost any web-application to it and start testing quickly.

### Installing

Just download this project to Python virtual environment on your local computer and install dependencies using file requirements.txt:

pip3 -r requirements.txt

You must install Java on your local machine to use Allure for the test reports.

Also, please set the path for your drivers in the file webdriverfactory.py, located ../demoTestingFramework-Python/base/ based on OS

### Running the tests

Use this command in the terminal from your virtual environment to run Demo Test Suite:

py.test tests/test_suite_demo.py 

or that for using chrome driver

py.test tests/test_suite_demo.py --browser chrome


### Getting the Allure reports

Use this command in the terminal from your virtual environment if you want to get the Allure report:

1. py.test tests/test_suite_demo.py --alluredir=allureress 

2. (Path to your project directory)../demoTestingFramework-Python/allure-2.10.0/bin/allure serve allureress

Example screenshots:

<img src="https://demo.meta-modern-up.com/allure_img/Allure001.png" width="500" target="_blank">
<img src="https://demo.meta-modern-up.com/allure_img/Allure002.png" width="500" target="_blank">
<img src="https://demo.meta-modern-up.com/allure_img/Allure003.png" width="500" target="_blank">
<img src="https://demo.meta-modern-up.com/allure_img/Allure004.png" width="500" target="_blank">
