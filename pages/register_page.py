from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def open_register(self):
        self.driver.get("https://stellarburgers.education-services.ru/register")

    def fill_name(self, name: str):
        self.fill(RegisterPageLocators.NAME_INPUT, name)

    def fill_email(self, email: str):
        self.fill(RegisterPageLocators.EMAIL_INPUT, email)

    def fill_password(self, password: str):
        self.fill(RegisterPageLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)