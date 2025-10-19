from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
from .locators import MainPageLocators, HeaderLocators


class MainPage(BasePage):
    def open_main(self):
        self.driver.get("https://stellarburgers.education-services.ru/")

    
    def go_account_from_header(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT)

    def go_constructor_from_header(self):
        self.click(HeaderLocators.CONSTRUCTOR)

    def go_constructor_by_logo(self):
        self.click(HeaderLocators.LOGO)

    def click_login_on_main(self):
        self.click(MainPageLocators.MAIN_LOGIN_BUTTON)

  
    def open_buns_tab(self):
        if self.is_tab_active("Булки"):
            return
        try:
            self.click(MainPageLocators.TAB_BUNS)
        except ElementClickInterceptedException:
            
            pass

    def open_sauces_tab(self):
        if self.is_tab_active("Соусы"):
            return
        try:
            self.click(MainPageLocators.TAB_SAUCES)
        except ElementClickInterceptedException:
            pass

    def open_fillings_tab(self):
        if self.is_tab_active("Начинки"):
            return
        try:
            self.click(MainPageLocators.TAB_FILLINGS)
        except ElementClickInterceptedException:
            pass

    def is_tab_active(self, tab_name: str) -> bool:
        by = MainPageLocators.ACTIVE_TAB_BY_NAME(tab_name)
        return self.is_visible(by, timeout=10)