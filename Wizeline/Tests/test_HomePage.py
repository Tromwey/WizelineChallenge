from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from Config.config import TestData
from Tests.test_base import BaseTest

import sys

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

import time

class Test_Home(BaseTest):
    def test_logout(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login()
        self.loginCheck = self.homePage.is_enabled(HomePage.BUTTON_SHOPPING_CART)
        assert self.loginCheck
        self.homePage.do_logout()
        assert self.homePage.is_enabled(LoginPage.USER)

    def test_sort_price_L2H(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login()
        self.loginCheck = self.homePage.is_enabled(HomePage.BUTTON_SHOPPING_CART)
        assert self.loginCheck
        self.homePage.do_sort(HomePage.OPTION_PRICE_L2H)
        self.elements = self.homePage.get_elements(HomePage.PRICES)
        assert self.elements[0].text == HomePage.PRICE_LOWEST
        assert self.elements[-1].text == HomePage.PRICE_HIGHEST
        

    def test_add_multiple_element_to_cart(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login()
        self.loginCheck = self.homePage.is_enabled(HomePage.BUTTON_SHOPPING_CART)
        assert self.loginCheck
        self.homePage.do_add_item_to_cart(HomePage.BUTTON_ADD2CART_SL_BACKPACK)
        self.homePage.do_add_item_to_cart(HomePage.BUTTON_ADD2CART_SL_BIKE_LIGHT)
        self.homePage.do_add_item_to_cart(HomePage.BUTTON_ADD2CART_SL_FLEECE_JACKET)
        self.homePage.do_click(HomePage.BUTTON_SHOPPING_CART)
        assert self.homePage.is_item_in_cart(HomePage.ITEM_SL_BACKPACK)
        assert self.homePage.is_item_in_cart(HomePage.ITEM_SL_BIKE_LIGHT)
        assert self.homePage.is_item_in_cart(HomePage.ITEM_SL_FLEECE_JACKET)

    def test_add_sl_onesie(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login()
        self.loginCheck = self.homePage.is_enabled(HomePage.BUTTON_SHOPPING_CART)
        assert self.loginCheck
        self.homePage.do_add_item_to_cart(HomePage.BUTTON_ADD2CART_SL_ONESIE)
        self.homePage.do_click(HomePage.BUTTON_SHOPPING_CART)
        assert self.homePage.is_item_in_cart(HomePage.ITEM_SL_ONESIE)