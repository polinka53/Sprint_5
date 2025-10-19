from selenium.webdriver.common.by import By


class HeaderLocators:
    # Кнопка "Личный Кабинет" в шапке
    PERSONAL_ACCOUNT = (By.XPATH, "//p[normalize-space()='Личный Кабинет']/..")
    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']/..")
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//*[@class and contains(@class,'AppHeader_header__logo')]//a")


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

    # Вкладки конструктора – кликаем по контейнеру .tab, а не по span
    TAB_BUNS     = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Булки']]")
    TAB_SAUCES   = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Соусы']]")
    TAB_FILLINGS = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Начинки']]")

    # Активная вкладка по тексту
    def ACTIVE_TAB_BY_NAME(name: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'tab') and contains(@class,'current')]//span[normalize-space()='{name}']",
        )


class LoginPageLocators:
    LOGIN_HEADER   = (By.XPATH, "//h2[normalize-space()='Вход']")
    EMAIL_INPUT    = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    SUBMIT_BUTTON  = (By.XPATH, "//button[normalize-space()='Войти']")
    REGISTER_LINK  = (By.XPATH, "//a[contains(@href,'/register')]")
    FORGOT_LINK    = (By.XPATH, "//a[contains(@href,'/forgot-password')]")


class RegisterPageLocators:
    NAME_INPUT      = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")
    EMAIL_INPUT     = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT  = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    LOGIN_LINK      = (By.XPATH, "//a[contains(@href,'/login')]")
    ERROR_TEXT      = (By.XPATH, "//*[text()='Некорректный пароль' or contains(., 'Некорректный пароль')]")


class AccountPageLocators:
    PROFILE_HEADER = (By.XPATH, "//h2[normalize-space()='Профиль']")
    LOGOUT_BUTTON  = (By.XPATH, "//button[normalize-space()='Выход']")