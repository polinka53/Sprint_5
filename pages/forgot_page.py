from .base_page import BasePage
from .locators import ForgotLocators

class ForgotPage(BasePage):
    def open_forgot(self):
        self.open("/forgot-password")

    def go_login(self):
        self.click(ForgotLocators.LOGIN_LINK)