from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage

import pytest
@pytest.mark.needs_auth
def test_login_from_register_form(driver, base_url, registered_user):
    reg = RegisterPage(driver, base_url)
    reg.open_register()

    login = LoginPage(driver, base_url)
    login.open_login()
    login.login(registered_user["email"], registered_user["password"])

    account = AccountPage(driver, base_url)
    account.open_account()
    assert account.is_profile_visible()


@pytest.mark.xfail(reason="Учебный стенд: авторизация временно не отвечает", strict=False)
def test_login_from_forgot_password(driver, base_url, registered_user):
    login = LoginPage(driver, base_url)
    login.open_forgot_password()
    login.open_login()
    login.login(registered_user["email"], registered_user["password"])

    account = AccountPage(driver, base_url)
    account.open_account()
    assert account.is_profile_visible()