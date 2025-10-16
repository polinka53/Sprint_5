from utils.generators import gen_email, gen_password, gen_name
from pages.register_page import RegisterPage
from pages.locators import LoginPageLocators  

def test_success_registration_redirects_to_login(driver, base_url):
    reg = RegisterPage(driver, base_url)
    reg.open_register()
    reg.fill_name(gen_name())
    reg.fill_email(gen_email())
    reg.fill_password(gen_password(min_len=6))
    reg.submit()
    
    assert reg.wait_url_contains("login", timeout=10)

def test_short_password_shows_validation_error(driver, base_url):
    reg = RegisterPage(driver, base_url)
    reg.open_register()
    reg.fill_name(gen_name())
    reg.fill_email(gen_email())
    reg.fill_password("12345")  
    reg.submit()
    assert reg.has_password_error()