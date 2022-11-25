import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _products = "menu-item-71"
    _pages = "menu-item-72"
    _my_account = "menu-item-77"
    _search_icon = "//*[@id='site-elementor-header']//*[contains(@class,'auxicon-search-4 auxicon')]"
    _cart_icon = "//*[@id='site-elementor-header']//*[contains(@class,'aux-shopping-basket aux-phone-off " \
                 "aux-action-on-hover')] "
    _checkout = "//*[@id='site-elementor-header']//*[contains(@class,'aux-inline-card-checkout')]//*[contains(text()," \
                "'Checkout')] "


    def navigateToProducts(self):
        self.elementClick(locator=self._products)

    def navigateToPages(self):
        self.elementClick(locator=self._pages)

    def navigateToMyAccount(self):
        self.elementClick(locator=self._my_account)

    def navigateToSearchIcon(self):
        self.elementClick(locator=self._search_icon, locatorType="xpath")

    def navigateToCheckout(self):
        self.elementClick(locator=self._checkout, locatorType="xpath")

    def navigateToCartIcon(self):
        self.elementClick(locator=self._cart_icon, locatorType="xpath")
