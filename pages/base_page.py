import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

BASE_URL = os.getenv("BASE_URL", "https://stellarburgers.education-services.ru")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Навигация ----------
    def open(self, path: str = "/"):
        if path.startswith("http"):
            url = path
        else:
            url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def wait_url_contains(self, part: str, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(part))
        return True

    # ---------- Поиск/ожидания ----------
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # ---------- Действия ----------
    def type(self, locator, text):
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        """
        Надёжный клик:
        1) ждём кликабельности;
        2) пробуем обычный click();
        3) при перехвате/устаревании пробуем ещё раз;
        4) как fallback — JS click.
        """
        last_exc = None
        for _ in range(3):
            try:
                el = self.wait_clickable(locator)
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                el.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                last_exc = e
        # fallback
        el = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].click();", el)
        if last_exc:
            
            _ = str(last_exc)

    def is_visible(self, locator, timeout=5):
        try:
            self.wait_visible(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False