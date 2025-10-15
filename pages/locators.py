from selenium.webdriver.common.by import By


class MainPageLocators:
    # Верхняя панель
    LOGIN_ACCOUNT_BUTTON  = (By.XPATH, "//button[.='Войти в аккаунт']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[.='Личный Кабинет' or .='Личный кабинет']")
    CONSTRUCTOR_LINK      = (By.XPATH, "//p[.='Конструктор']")
    LOGO_LINK             = (By.XPATH, "//div[contains(@class,'AppHeader')]/a")

    # Табы «Конструктор»
    BUNS_TAB      = (By.XPATH, "//span[.='Булки']/..")
    SAUCES_TAB    = (By.XPATH, "//span[.='Соусы']/..")
    FILLINGS_TAB  = (By.XPATH, "//span[.='Начинки']/..")

    # Активный таб
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")

    BUNS_SECTION_TITLE     = (By.XPATH, "//h2[.='Булки']")
    SAUCES_SECTION_TITLE   = (By.XPATH, "//h2[.='Соусы']")
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[.='Начинки']")


class LoginPageLocators:
    EMAIL_INPUT    = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON   = (By.XPATH, "//button[text()='Войти']")
    PASS_INPUT = PASSWORD_INPUT  


class RegisterPageLocators:
    NAME_INPUT      = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT     = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT  = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_TEXT      = (By.XPATH, "//p[@class='input__error text_type_main-default']")


class AccountPageLocators:
    PROFILE_HEADER = (By.XPATH, "//*[text()='Профиль']")
    LOGOUT_BUTTON_TEXT     = (By.XPATH, "//button[normalize-space()='Выйти' or normalize-space()='Выход']")
    LOGOUT_BUTTON_CONTAINS = (By.XPATH, "//button[contains(.,'Выйт') or contains(.,'Выход')]")
    LOGOUT_BUTTON_ANY      = (By.XPATH, "//*[self::button or self::a][contains(.,'Выйт') or contains(.,'Выход')]")

    LOGOUT_BUTTON = LOGOUT_BUTTON_ANY


class ForgotLocators:
    EMAIL_INPUT    = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK     = (By.XPATH, "//a[text()='Войти']")


class CommonLocators:
    LOADER = (By.XPATH, "//*[contains(@class,'Loader') or contains(@class,'loading')]")


class ConstructorLocators:
    BUNS_SECTION     = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION   = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")