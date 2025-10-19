from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    
    def open(self, url: str):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            
            self.driver.get(self.driver.current_url.split("/", 3)[0] + "//" + self.driver.current_url.split("/", 3)[2] + url)

    def wait_visible(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, locator):
        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    def click(self, locator, timeout: int = DEFAULT_TIMEOUT):
        
        try:
            self.wait_clickable(locator, timeout).click()
            return
        except ElementClickInterceptedException:
            pass  

        el = self.scroll_into_view(locator)
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            el.click()
        except ElementClickInterceptedException:
            
            WebDriverWait(self.driver, 1).until(lambda d: True)
            el.click()

    def fill(self, locator, text: str):
        field = self.wait_visible(locator)
        field.clear()
        field.send_keys(text)

    def is_visible(self, locator, timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False