from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.locators import AccountPageLocators, MainPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def is_profile_opened(self):
        """Проверяет, открыт ли личный кабинет пользователя"""
        url = (self.current_url() or "")
        if "account" in url:
            return True

        # Ждём заголовок «Профиль»
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(AccountPageLocators.PROFILE_HEADER)
            )
            return True
        except TimeoutException:
            pass

        # Проверяем наличие любой кнопки «Выйти» — про запас
        for loc in (
            AccountPageLocators.LOGOUT_BUTTON_TEXT,
            AccountPageLocators.LOGOUT_BUTTON_CONTAINS,
            AccountPageLocators.LOGOUT_BUTTON_ANY,
        ):
            try:
                if self.driver.find_elements(*loc):
                    return True
            except Exception:
                pass
        return False

    def open_account(self):
        self.open("/account/profile")

    def logout(self):
        """Нажимает кнопку 'Выйти'"""
        try:
            
            for loc in (
                AccountPageLocators.LOGOUT_BUTTON_TEXT,
                AccountPageLocators.LOGOUT_BUTTON_CONTAINS,
                AccountPageLocators.LOGOUT_BUTTON_ANY,
            ):
                elements = self.driver.find_elements(*loc)
                if elements:
                    elements[0].click()
                    return
            raise Exception("Кнопка 'Выйти' не найдена")
        except Exception as e:
            print(f"[Ошибка logout]: {e}")

    # --- Переходы ---
    def go_constructor(self):
        """Переход к конструктору"""
        self.click(MainPageLocators.CONSTRUCTOR_LINK)