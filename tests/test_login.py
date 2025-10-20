from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, HeaderLocators
from conftest import BASE_URL

def _login(driver, email, password):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators["EMAIL_INPUT"])
    ).send_keys(email)
    driver.find_element(*LoginPageLocators["PASSWORD_INPUT"]).send_keys(password)
    driver.find_element(*LoginPageLocators["SUBMIT_BUTTON"]).click()

def test_login_from_main_button(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element("xpath", "//button[normalize-space()='Войти в аккаунт']").click()
    _login(driver, registered_user["email"], registered_user["password"])
    WebDriverWait(driver, 10).until_not(EC.url_contains("/login"))
    assert driver.current_url.startswith(BASE_URL)

def test_login_from_header_account(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*HeaderLocators["PERSONAL_ACCOUNT"]).click()
    _login(driver, registered_user["email"], registered_user["password"])
    WebDriverWait(driver, 10).until_not(EC.url_contains("/login"))
    assert driver.current_url.startswith(BASE_URL)