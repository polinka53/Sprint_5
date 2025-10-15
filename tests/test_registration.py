from pages.locators import RegisterPageLocators

def test_success_registration(driver, pages, new_user):
    pages["register"].open_register()
    pages["register"].register(new_user["name"], new_user["email"], new_user["password"])
    
    pages["login"].wait_login_page_opened()
    assert "login" in pages["login"].current_url()

def test_error_on_short_password(driver, pages, new_user):
    pages["register"].open_register()
    pages["register"].register(new_user["name"], new_user["email"], "12345")
    assert pages["register"].is_visible(RegisterPageLocators.ERROR_TEXT)
    