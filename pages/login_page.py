from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators

class LoginPage(BasePage):
    def open_login(self):
        self.open("/login")

    def open_forgot_password(self):
        self.open("/forgot-password")

    def is_login_visible(self) -> bool:
        return self.is_visible(LoginPageLocators.LOGIN_HEADER)

    def login(self, email: str, password: str):
        """Авторизация пользователя через форму входа."""
        self.type(RegisterPageLocators.EMAIL_INPUT, email)
        self.type(RegisterPageLocators.PASSWORD_INPUT, password)
        
        from selenium.webdriver.common.by import By
        self.click((By.XPATH, "//button[text()='Войти']"))