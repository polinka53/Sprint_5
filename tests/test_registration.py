from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
from conftest import BASE_URL

def test_success_registration_redirects_to_login(driver, unique_user):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*RegisterPageLocators["NAME_INPUT"]).send_keys(unique_user["name"])
    driver.find_element(*RegisterPageLocators["EMAIL_INPUT"]).send_keys(unique_user["email"])
    driver.find_element(*RegisterPageLocators["PASSWORD_INPUT"]).send_keys(unique_user["password"])
    driver.find_element(*RegisterPageLocators["SUBMIT_BUTTON"]).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url