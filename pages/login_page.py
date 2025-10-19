from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def open_login(self):
        self.driver.get("https://stellarburgers.education-services.ru/login")

    def fill_email(self, email: str):
        self.fill(LoginPageLocators.EMAIL_INPUT, email)

    def fill_password(self, password: str):
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)