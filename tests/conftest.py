import pytest
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.register_page import RegisterPage


BASE_URL = "https://stellarburgers.education-services.ru/"


def _rand(n=3) -> str:
    return "".join(random.choices(string.digits, k=n))


@pytest.fixture
def driver():
    """Старт/стоп браузера на каждый тест."""
    options = Options()
    options.add_argument("--window-size=1280,900")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    # options.add_argument("--headless=new")  # если захочешь гонять без UI

    drv = webdriver.Chrome(service=Service(), options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def registered_user(driver):
    """
    Готовит валидного пользователя через UI и возвращает его креды.
    После регистрации остаёмся на /login — далее тесты сами логинятся.
    """
    name = "Polina"
    email = f"polina_pavl_1999_{_rand()}@yandex.ru"
    password = "123456"

    reg = RegisterPage(driver)
    reg.open_register()         
    reg.fill_name(name)
    reg.fill_email(email)
    reg.fill_password(password)
    reg.submit()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    return {"name": name, "email": email, "password": password}


@pytest.fixture
def unique_user():
    """Если где-то нужен просто уникальный юзер без предварительной регистрации."""
    return {
        "name": "Polina",
        "email": f"polina_pavl_1999_{_rand()}@yandex.ru",
        "password": "123456",
    }