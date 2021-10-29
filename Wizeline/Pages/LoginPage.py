from selenium.webdriver.common.by import By

from Config.config import TestData

from Pages.BasePage import BasePage

class LoginPage(BasePage):

    USER = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    MESSAGE_ERROR = (By.CSS_SELECTOR, "h3")

    TEXT_INVALID_LOGIN = "Epic sadface: Username and password do not match any user in this service"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USER, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.BUTTON_LOGIN)

    def get_message_error(self):
        return self.get_element_text(self.MESSAGE_ERROR)
