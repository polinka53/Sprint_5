def test_go_to_personal_account(driver, pages, registered_user):
    pages["main"].open("/")
    pages["main"].go_personal_account()
    pages["login"].login(registered_user["email"], registered_user["password"])

    pages["account"].open_account()
    assert pages["account"].is_profile_opened()

