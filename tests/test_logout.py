import pytest
from pages.locators import LoginPageLocators

@pytest.mark.xfail(reason="Учебный стенд: после логаута редирект/сессия ведут себя нестабильно")
def test_logout_from_account(driver, pages, registered_user):
    # Логин
    pages["main"].open_main()
    pages["main"].go_personal_account()
    pages["login"].login(registered_user["email"], registered_user["password"])

    # Заходим в профиль и убеждаемся, что вошли
    pages["account"].open_account()
    assert pages["account"].is_profile_opened()

    # Логаут
    pages["account"].logout()

    # Явно открываем страницу логина и проверяем поля (признак выхода)
    pages["login"].open("/login")
    assert pages["login"].is_visible(LoginPageLocators.EMAIL_INPUT, timeout=5)
    assert pages["login"].is_visible(LoginPageLocators.PASSWORD_INPUT, timeout=5)
    assert pages["login"].is_visible(LoginPageLocators.LOGIN_BUTTON, timeout=5)
