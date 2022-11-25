from pages.buying.buying_dress_page import BuyingBlackDress
from utilities.testingstatus import TestingStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import unittest
import pytest
import allure


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class BuyingDressTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.buying = BuyingBlackDress(self.driver)
        self.ts = TestingStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/seva/Documents/00-Projects/DemoFrameWork/testdata.csv"))
    @unpack
    @allure.feature("Buying dress with invalid payment data")
    @allure.story("Putting dress into cart and try to check out with invalid payment method")
    @allure.severity("blocker")
    def test_invalidPayOptions(self, dressName):
        """
        in this test we try to put dress into cart and try to check out with invalid payment method
        """
        self.buying.clickSearchIcon()
        self.buying.enterDressName(dressName)
        self.buying.clickNextSearchIcon()
        self.buying.clickAddToCart()
        self.buying.clickCartIcon()
        self.buying.clickCheckout()
        self.buying.clickPlaceOrder()
        result = self.buying.verifyInvalidPaymentMethod()
        self.ts.markFinal("test_invalidPayMethod", result,
                          "Payment Failed Verification")
