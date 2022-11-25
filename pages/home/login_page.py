import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _my_account = "menu-item-77"
    _user_field = "username"
    _password_field = "password"
    _login_button = "login"

    def clickMyAccountLink(self):
        self.elementClick(self._my_account, locatorType="id")

    def enterUsername(self, username):
        self.sendKeys(username, self._user_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id" )

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, username="", password=""):
        self.clickMyAccountLink()
        self.clearFields()
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//*[contains(text(),'Hello')]",
                            locatorType="xpath")
        result = self.isElementPresent(locator="//*[contains(text(),'Hello')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//strong[contains(text(),'Error:')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My account – test_ecommerce")

    def logout(self):
        self.elementClick(locator="Log out",
                          locatorType="Link")

    def clearFields(self):
        usernameField = self.getElement(locator=self._user_field)
        usernameField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
