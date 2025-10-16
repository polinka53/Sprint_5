from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def open_register(self):
        self.open("/register")

    # Заполнение имени
    def fill_name(self, text):
        self.type(RegisterPageLocators.NAME_INPUT, text)

    # Заполнение email
    def fill_email(self, text):
        self.type(RegisterPageLocators.EMAIL_INPUT, text)

    # Заполнение пароля
    def fill_password(self, text):
        self.type(RegisterPageLocators.PASSWORD_INPUT, text)

    # Клик по кнопке "Зарегистрироваться"
    def submit(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    # Проверка, что произошёл переход на страницу логина
    def is_login_redirect(self):
        return self.wait_url_contains("/login")

    # Проверка появления ошибки при некорректном пароле
    def has_password_error(self):
        return self.is_visible((By.XPATH, "//p[text()='Некорректный пароль']"), timeout=5)