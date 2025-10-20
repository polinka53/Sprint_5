from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPageLocators
from conftest import BASE_URL

def test_go_to_personal_account_opens_profile(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*HeaderLocators["PERSONAL_ACCOUNT"]).click()

    driver.find_element(*LoginPageLocators["EMAIL_INPUT"]).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators["PASSWORD_INPUT"]).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators["SUBMIT_BUTTON"]).click()

    driver.find_element(*HeaderLocators["PERSONAL_ACCOUNT"]).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url