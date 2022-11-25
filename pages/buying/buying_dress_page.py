import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class BuyingBlackDress(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    ################
    ### Locators ###
    ################
    # _search_icon = "//*[@id='site-elementor-header']//*[contains(@class,'auxicon-search-4 auxicon')]"
    _search_data = "//*[@id='site-elementor-header']//*[contains(@class,'aux-search-field')]"
    _next_search_icon = "//*[@id='site-elementor-header']//*[contains(@class,'aux-iconic-search-submit')]"
    _add_to_cart = "//*[@id='primary']//*[text()='Add to cart']"
    # _cart_icon = "//*[@id='site-elementor-header']//*[contains(@class,'aux-shopping-basket aux-phone-off " \
    #              "aux-action-on-hover')] "
    # _checkout = "//*[@id='site-elementor-header']//*[contains(@class,'aux-inline-card-checkout')]//*[contains(text()," \
    #             "'Checkout')] "
    _place_order = "//*[@id='place_order']"
    _invalid_payment_message = "//*[@id='post-59']//*[@data-id='billing_phone']//following-sibling::li"

    def clickSearchIcon(self):
        self.nav.navigateToSearchIcon()

    def enterDressName(self, name):
        self.sendKeys(name, locator=self._search_data, locatorType="xpath")

    def clickNextSearchIcon(self):
        self.elementClick(locator=self._next_search_icon, locatorType="xpath")

    def clickAddToCart(self):
        self.elementClick(locator=self._add_to_cart, locatorType="xpath")

    def clickCartIcon(self):
        self.nav.navigateToCartIcon()

    def clickCheckout(self):
        self.nav.navigateToCheckout()

    def clickPlaceOrder(self):
        self.webScroll(direction="down")
        self.util.sleep(5)
        self.elementClick(locator=self._place_order, locatorType="xpath")

    def verifyInvalidPaymentMethod(self):
        messageElement = self.waitForElement(self._invalid_payment_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

