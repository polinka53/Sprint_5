from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage


def test_success_registration_redirects_to_login(driver, unique_user):
    reg = RegisterPage(driver)
    reg.open_register()
    reg.fill_name(unique_user["name"])
    reg.fill_email(unique_user["email"])
    reg.fill_password(unique_user["password"])
    reg.submit()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url