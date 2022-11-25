from pages.buying.buying_dress_page import BuyingBlackDress
from utilities.testingstatus import TestingStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BuyingDressTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.buying = BuyingBlackDress(self.driver)
        self.ts = TestingStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidPayOptions(self):
        self.buying.clickSearchIcon()
        self.buying.enterDressName('Black Maxi Dress')
        self.buying.clickNextSearchIcon()
        self.buying.clickAddToCart()
        self.buying.clickCartIcon()
        self.buying.clickCheckout()
        self.buying.clickPlaceOrder()
        result = self.buying.verifyInvalidPaymentMethod()
        self.ts.markFinal("test_invalidPayMethod", result,
                          "Payment Failed Verification")
