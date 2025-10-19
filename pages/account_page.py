from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import AccountPageLocators


class AccountPage(BasePage):
    def open_account(self):
        
        self.driver.get("https://stellarburgers.education-services.ru/account/profile")

    def is_profile_visible(self) -> bool:
        
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("/account"))
            return self.is_visible(AccountPageLocators.LOGOUT_BUTTON, timeout=5)
        except Exception:
            return False

    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)