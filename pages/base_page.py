import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException

class BasePage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    # Навигация
    def open(self, path: str = "/"):
        path = "/" + path.lstrip("/")
        self.driver.get(self.base_url + path)

    # Ожидания/поиск
    def find(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout: int = 10):
        """Аккуратный клик: прокрутка → наведение → клик; с повтором при перехвате."""
        end = time.time() + timeout
        last_err = None
        while True:
            try:
                el = self.wait_clickable(locator, timeout=max(1, int(end - time.time())))
                self.scroll_into_view(locator)
                ActionChains(self.driver).move_to_element(el).pause(0.05).click(el).perform()
                return
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                last_err = e
                if time.time() >= end:
                    raise last_err
                time.sleep(0.2)

    def type(self, locator, text: str):
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

    # Вспомогательные
    def get_attr(self, locator, attribute: str):
        el = self.wait_visible(locator)
        return el.get_attribute(attribute)

    def is_visible(self, locator, timeout: int = 10) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except Exception:
            return False

    def scroll_into_view(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

    def wait_url_contains(self, substring: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))
            return True
        except Exception:
            return False