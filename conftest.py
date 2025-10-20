import pytest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegisterPageLocators

BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"

def random_string(n=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1280,900")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

@pytest.fixture
def unique_user():
    email = f"polina_pavl_1999_{int(time.time()) % 100000}{random_string(3)}@yandex.ru"
    return {"name": "Polina", "email": email, "password": "123456"}

@pytest.fixture
def registered_user(driver, unique_user):
    driver.get(f"{BASE_URL}/register")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators["NAME_INPUT"])
    ).send_keys(unique_user["name"])
    driver.find_element(*RegisterPageLocators["EMAIL_INPUT"]).send_keys(unique_user["email"])
    driver.find_element(*RegisterPageLocators["PASSWORD_INPUT"]).send_keys(unique_user["password"])
    driver.find_element(*RegisterPageLocators["SUBMIT_BUTTON"]).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    return unique_user