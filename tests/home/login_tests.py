import allure
from pages.home.login_page import LoginPage
from utilities.testingstatus import TestingStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestingStatus(self.driver)

    @pytest.mark.run(order=1)
    @allure.feature("Login with invalid data")
    @allure.story("Open Login page and try to sine in with invalid data")
    @allure.severity("blocker")
    def test_t1invalidLogin(self):
        """
        in this test we try to log in with invalid username and password
        """
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("222", "333")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    @allure.feature("Login with valid data")
    @allure.story("Open Login page and try to signe in with valid data")
    @allure.severity("blocker")
    def test_t2validLogin(self):
        """
        in this test we are loging in with valid username and password
        """
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.login("tester", "tester-12345")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t2validLogin", result2, "Login Verification")
