from selenium.webdriver.common.by import By

from Config.config import TestData

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


class CartPage(BasePage):

    BUTTON_CHECKOUT = (By.ID, "checkout")

    FIRST_NAME = (By.ID ,"first-name")
    LAST_NAME  = (By.ID ,"last-name")
    ZIP_CODE   = (By.ID ,"postal-code")

    BUTTON_CONTINUE = (By.ID, "continue")
    BUTTON_FINISH = (By.ID, "finish")

    HEADER_COMPLETE = (By.CLASS_NAME, "complete-text")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self):
        self.do_send_keys(LoginPage.USER, TestData.USERNAME_VALID_01)
        self.do_send_keys(LoginPage.PASSWORD, TestData.PASSWORD_VALID)
        self.do_click(LoginPage.BUTTON_LOGIN)

    def do_add_backpack_to_cart(self):
        self.do_click(HomePage.BUTTON_ADD2CART_SL_BACKPACK)

