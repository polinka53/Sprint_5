from .base_page import BasePage
from .locators import AccountPageLocators, LoginPageLocators

class AccountPage(BasePage):
    def open_account(self):
        """Открывает страницу профиля."""
        self.open("/account")

    def is_profile_visible(self):
        
        return self.is_visible(AccountPageLocators.PROFILE_HEADER, timeout=15)

    def logout(self):
        """Нажимает кнопку 'Выход' и ждёт появления формы входа."""
        self.click(LoginPageLocators.LOGOUT_BUTTON_CONTAINS)
        return self.is_visible(LoginPageLocators.LOGIN_HEADER, timeout=15)