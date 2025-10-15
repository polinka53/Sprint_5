import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from pages.forgot_page import ForgotPage
from pages.constructor_page import ConstructorPage
from utils.generators import gen_email, gen_password, gen_name

load_dotenv()

@pytest.fixture
def driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "1") == "1"

    if browser == "firefox":
        options = FirefoxOptions()
        if headless: options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if headless: options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        drv = webdriver.Chrome(options=options)

    drv.implicitly_wait(5)
    yield drv
    drv.quit()

@pytest.fixture
def pages(driver):
    return {
        "main": MainPage(driver),
        "login": LoginPage(driver),
        "register": RegisterPage(driver),
        "account": AccountPage(driver),
        "forgot": ForgotPage(driver),
        "constructor": ConstructorPage(driver),
    }

@pytest.fixture
def new_user():
    return {"name": gen_name(), "email": gen_email(), "password": gen_password()}

@pytest.fixture
def registered_user(driver, pages, new_user):
    pages["register"].open("/register")
    pages["register"].register(new_user["name"], new_user["email"], new_user["password"])
    pages["login"].login(new_user["email"], new_user["password"])
    return new_user
