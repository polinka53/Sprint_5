from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage

import pytest
@pytest.mark.needs_auth

def test_go_to_personal_account_opens_profile(driver, base_url, registered_user):
    main = MainPage(driver, base_url)
    main.open_main()

    login = LoginPage(driver, base_url)
    login.open_login()
    login.login(registered_user["email"], registered_user["password"])

    account = AccountPage(driver, base_url)
    account.open_account()
    assert account.is_profile_visible()