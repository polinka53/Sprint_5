from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common import TimeoutException

class MainPage(BasePage):
    def open_main(self):
        self.open("/")

    def open_buns_tab(self):
        self.click(MainPageLocators.TAB_BUNS)

    def open_sauces_tab(self):
        self.click(MainPageLocators.TAB_SAUCES)

    def open_fillings_tab(self):
        self.click(MainPageLocators.TAB_FILLINGS)

    def is_tab_active(self, tab_name: str) -> bool:
        
        by = MainPageLocators.ACTIVE_TAB_BY_NAME(tab_name)
        try:
            self.wait_visible(by, timeout=5)
            return True
        except TimeoutException:
            return False