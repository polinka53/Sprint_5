from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPageLocators, AccountPageLocators
from conftest import BASE_URL

def test_logout_from_account(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*HeaderLocators["PERSONAL_ACCOUNT"]).click()

    driver.find_element(*LoginPageLocators["EMAIL_INPUT"]).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators["PASSWORD_INPUT"]).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators["SUBMIT_BUTTON"]).click()

    WebDriverWait(driver, 10).until_not(EC.url_contains("/login"))

    driver.find_element(*HeaderLocators["PERSONAL_ACCOUNT"]).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AccountPageLocators["LOGOUT_BUTTON"])
    ).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url