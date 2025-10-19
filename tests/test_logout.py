from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_logout_from_account(driver, registered_user):
    
    main = MainPage(driver)
    main.open_main()
    main.go_account_from_header()

    login = LoginPage(driver)
    login.fill_email(registered_user["email"])
    login.fill_password(registered_user["password"])
    login.submit()

    main.go_account_from_header()
    acc = AccountPage(driver)
    assert acc.is_profile_visible()

    
    acc.logout()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))