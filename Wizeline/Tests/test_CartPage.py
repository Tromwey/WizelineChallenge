from Config.config import TestData
from Tests.test_base import BaseTest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.CartPage import CartPage

import time

class Test_Cart(BaseTest):

    def test_checkout(self):
        self.cartPage = CartPage(self.driver)
        self.cartPage.do_login()
        self.loginCheck = self.cartPage.is_enabled(HomePage.BUTTON_SHOPPING_CART)
        assert self.loginCheck
        self.cartPage.do_add_backpack_to_cart()
        self.cartPage.do_click(HomePage.BUTTON_SHOPPING_CART)
        self.cartCheck = self.cartPage.is_enabled(CartPage.BUTTON_CHECKOUT)
        assert self.cartCheck
        self.cartPage.do_click(CartPage.BUTTON_CHECKOUT)
        self.cartPage.do_send_keys(CartPage.FIRST_NAME, TestData.FIRST_NAME)
        self.cartPage.do_send_keys(CartPage.LAST_NAME, TestData.LAST_NAME)
        self.cartPage.do_send_keys(CartPage.ZIP_CODE, TestData.ZIP_CODE)
        self.cartPage.do_click(CartPage.BUTTON_CONTINUE)
        self.cartPage.do_click(CartPage.BUTTON_FINISH)
        self.completeCheck = self.cartPage.is_enabled(CartPage.HEADER_COMPLETE)
        assert self.completeCheck


