from selenium.webdriver.common.by import By

class MainPageLocators:
    TAB_BUNS     = (By.XPATH, "//span[text()='Булки']")
    TAB_SAUCES   = (By.XPATH, "//span[text()='Соусы']")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB_BY_NAME = lambda name: (
        By.XPATH,
        f"//div[contains(@class,'tab') and contains(@class,'current')]//span[text()='{name}']"
    )

class AccountPageLocators:
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")
    LOGOUT_BUTTON  = (By.XPATH, "//button[contains(., 'Выход')]")  

class LoginPageLocators:
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT  = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SUBMIT_BUTTON  = (By.XPATH, "//button[text()='Войти']")
    FORGOT_LINK    = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
    LOGIN_LINK     = (By.XPATH, "//a[contains(@href,'/login')]")  

class RegisterPageLocators:
    NAME_INPUT      = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT     = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT  = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_TEXT      = (By.XPATH, "//*[text()='Некорректный пароль' or contains(., 'Некорректный пароль')]")