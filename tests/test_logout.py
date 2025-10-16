from pages.login_page import LoginPage
from pages.account_page import AccountPage

import pytest
@pytest.mark.needs_auth

def test_logout_shows_login_page(driver, base_url, registered_user):
    login = LoginPage(driver, base_url)
    login.open_login()
    login.login(registered_user["email"], registered_user["password"])

    account = AccountPage(driver, base_url)
    account.open_account()
    assert account.is_profile_visible()

    assert account.logout()
    
    assert login.is_login_visible()