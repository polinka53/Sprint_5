from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):
    def open_register(self):
        self.open("/register")

    def register(self, name, email, password):
        self.type(RegisterPageLocators.NAME_INPUT, name)
        self.type(RegisterPageLocators.EMAIL_INPUT, email)
        self.type(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click(RegisterPageLocators.REGISTER_BUTTON)
        try:
            self.wait_url_contains("login", timeout=10)
        except Exception:
            pass

    def error_shown(self):
        return self.is_visible(RegisterPageLocators.ERROR_TEXT, timeout=5)