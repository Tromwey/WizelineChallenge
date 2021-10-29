from Config.config import TestData
from Tests.test_base import BaseTest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class Test_Login(BaseTest):

    def test_login_valid(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME_VALID_01, TestData.PASSWORD_VALID)
        assert self.loginPage.is_enabled(HomePage.BUTTON_SHOPPING_CART)

    def test_login_invalid_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME_INVALID, TestData.PASSWORD_VALID)
        message = self.loginPage.get_message_error()
        assert message == LoginPage.TEXT_INVALID_LOGIN

