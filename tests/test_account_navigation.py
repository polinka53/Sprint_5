from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage

def test_go_to_personal_account_opens_profile(driver, registered_user):
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