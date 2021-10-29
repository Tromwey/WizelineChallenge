from selenium.webdriver.common.by import By

from Config.config import TestData

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage

class HomePage(BasePage):

    BUTTON_MENU          = (By.ID, "react-burger-menu-btn")
    BUTTON_LOGOUT        = (By.ID, "logout_sidebar_link")
    BUTTON_SHOPPING_CART = (By.ID, "shopping_cart_container")

    BUTTON_ADD2CART_SL_BACKPACK                 = (By.ID, "add-to-cart-sauce-labs-backpack")
    BUTTON_ADD2CART_SL_BIKE_LIGHT               = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BUTTON_ADD2CART_SL_BOLT_TSHIRT              = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BUTTON_ADD2CART_SL_FLEECE_JACKET            = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    BUTTON_ADD2CART_SL_ONESIE                   = (By.ID, "add-to-cart-sauce-labs-onesie")
    BUTTON_ADD2CART_SL_TEST_ALLTHETHINGS_TSHIRT = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    COMBOBOX_SORT    = (By.CLASS_NAME, "product_sort_container")
    OPTION_NAME_A2Z  = (By.XPATH, "//*[text()='Name (A to Z)']")
    OPTION_NAME_Z2A  = (By.XPATH, "//*[text()='Name (Z to A)']")
    OPTION_PRICE_L2H = (By.XPATH, "//*[text()='Price (low to high)']")
    OPTION_PRICE_H2L = (By.XPATH, "//*[text()='Price (high to low)']")


    ITEM_SL_BACKPACK                 = (By.ID, "item_4_title_link")
    ITEM_SL_BIKE_LIGHT               = (By.ID, "item_0_title_link")
    ITEM_SL_BOLT_TSHIRT              = (By.ID, "item_1_title_link")
    ITEM_SL_FLEECE_JACKET            = (By.ID, "item_5_title_link")
    ITEM_SL_ONESIE                   = (By.ID, "item_2_title_link")
    ITEM_SL_TEST_ALLTHETHINGS_TSHIRT = (By.ID, "item_3_title_link")

    PRICES = (By.CLASS_NAME, "inventory_item_price")
    NAMES = (By.CLASS_NAME, "inventory_item_name")

    PRICE_LOWEST = "$7.99"
    PRICE_HIGHEST = "$49.99"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self):
        self.do_send_keys(LoginPage.USER, TestData.USERNAME_VALID_01)
        self.do_send_keys(LoginPage.PASSWORD, TestData.PASSWORD_VALID)
        self.do_click(LoginPage.BUTTON_LOGIN)

    def do_logout(self):
        self.do_click(self.BUTTON_MENU)
        self.do_click(self.BUTTON_LOGOUT)

    def do_add_item_to_cart(self, item):
        self.do_click(item)

    def do_sort(self, option):
        self.do_click(option)


    def is_item_in_cart(self, item):
        return self.is_enabled(item)