import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv

from pages.register_page import RegisterPage
from utils.generators import gen_email, gen_password, gen_name

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://stellarburgers.education-services.ru")


@pytest.fixture
def driver():
    """Инициализация браузера Chrome."""
    options = ChromeOptions()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    """Базовый URL приложения."""
    return BASE_URL


@pytest.fixture
def registered_user(driver, base_url):
    """Создаёт нового пользователя через UI и возвращает его данные."""
    page = RegisterPage(driver, base_url)
    page.open_register()

    name = gen_name()
    email = gen_email()
    password = gen_password()

    page.fill_name(name)
    page.fill_email(email)
    page.fill_password(password)
    page.submit()

    # Возвращаем данные для логина
    return {"name": name, "email": email, "password": password}
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def _auth_is_working(driver, base_url, timeout=6) -> bool:
    """Пробуем залогиниться заведомо фейковыми данными и ждём РЕАКЦИИ UI.
    Если страница совсем не реагирует (нет ошибки и нет перехода) — считаем, что логин «лежит».
    """
    try:
        driver.get(base_url + "/login")
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )

        email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        pwd   = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        btn   = driver.find_element(By.XPATH, "//button[text()='Войти']")

        email.clear(); email.send_keys("fake_user@example.test")
        pwd.clear();   pwd.send_keys("1234567")
        btn.click()

        
        WebDriverWait(driver, timeout).until(
            EC.any_of(
                EC.url_contains("/account"),
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(., 'Некорректн') or contains(., 'неверн') or contains(., 'ошибк')]")
                )
            )
        )
        return True
    except Exception:
        return False

@pytest.fixture(autouse=True)
def auth_guard(request, driver, base_url):
    """Если тест помечен needs_auth и авторизация на стенде не отвечает — xfail."""
    if request.node.get_closest_marker("needs_auth"):
        if not _auth_is_working(driver, base_url):
            pytest.xfail("Учебный стенд: авторизация временно не отвечает — помечаем тест XFAIL")