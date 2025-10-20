from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from conftest import BASE_URL

def test_switch_to_sauces_tab(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators["TAB_SAUCES"])
    ).click()
    text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators["TAB_ACTIVE_TEXT"])
    ).text
    assert text == "Соусы"

def test_switch_to_buns_tab(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators["TAB_SAUCES"])
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators["TAB_BUNS"])
    ).click()
    text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators["TAB_ACTIVE_TEXT"])
    ).text
    assert text == "Булки"

def test_switch_to_fillings_tab(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators["TAB_FILLINGS"])
    ).click()
    text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators["TAB_ACTIVE_TEXT"])
    ).text
    assert text == "Начинки"