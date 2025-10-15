def test_login_from_register_form(driver, pages, new_user):
    pages["register"].open_register()
    pages["register"].register(new_user["name"], new_user["email"], new_user["password"])


    pages["login"].open("/login")
    pages["login"].login(new_user["email"], new_user["password"])


    pages["account"].open_account()
    assert pages["account"].is_profile_opened()


def test_login_from_forgot_password(driver, pages, registered_user):
    pages["forgot"].open_forgot()
    pages["forgot"].go_login()
    pages["login"].wait_login_page_opened()
    pages["login"].login(registered_user["email"], registered_user["password"])

    
    pages["account"].open_account()
    assert pages["account"].is_profile_opened()