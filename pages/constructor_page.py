from .base_page import BasePage
from .locators import ConstructorLocators

class ConstructorPage(BasePage):
    def is_buns_visible(self):
        return self.is_visible(ConstructorLocators.BUNS_SECTION)

    def is_sauces_visible(self):
        return self.is_visible(ConstructorLocators.SAUCES_SECTION)

    def is_fillings_visible(self):
        return self.is_visible(ConstructorLocators.FILLINGS_SECTION)
    