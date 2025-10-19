from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_login_from_main_button(driver, registered_user):
    main = MainPage(driver)
    main.open_main()
    main.click_login_on_main()

    login = LoginPage(driver)
    login.fill_email(registered_user["email"])
    login.fill_password(registered_user["password"])
    login.submit()

   
    WebDriverWait(driver, 10).until_not(EC.url_contains("/login"))
    
    assert driver.current_url.rstrip("/").endswith("stellarburgers.education-services.ru")