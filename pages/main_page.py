from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def open_main(self):
        self.open("/")

    def click_login_account(self):
        self.click(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    def go_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_LINK)


    def open_buns_tab(self):
        self.click(MainPageLocators.BUNS_TAB)

    def open_sauces_tab(self):
        self.click(MainPageLocators.SAUCES_TAB)

    def open_fillings_tab(self):
        self.click(MainPageLocators.FILLINGS_TAB)
