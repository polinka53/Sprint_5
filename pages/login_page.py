from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, email, password):
        self.type(LoginPageLocators.EMAIL_INPUT, email)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def wait_login_page_opened(self):
        return self.wait_url_contains("login", timeout=10)