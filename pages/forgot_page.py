from .base_page import BasePage
from .locators import ForgotPageLocators

class ForgotPage(BasePage):
    def open_forgot(self):
        self.open("/forgot-password")

    def go_login(self):
        self.click(ForgotPageLocators.TO_LOGIN_LINK)