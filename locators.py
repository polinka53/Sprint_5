from selenium.webdriver.common.by import By

# ---------- Хедер ----------
HeaderLocators = {
    "PERSONAL_ACCOUNT": (By.XPATH, "//a[normalize-space()='Личный Кабинет']"),
}

# ---------- Страница входа ----------
LoginPageLocators = {
    "EMAIL_INPUT": (By.XPATH, "//input[@name='name' or @type='text' or @placeholder='Email']"),
    "PASSWORD_INPUT": (By.XPATH, "//input[@type='password']"),
    "SUBMIT_BUTTON": (By.XPATH, "//button[normalize-space()='Войти']"),
}

# ---------- Страница регистрации ----------
RegisterPageLocators = {
    "NAME_INPUT": (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input"),
    "EMAIL_INPUT": (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input"),
    "PASSWORD_INPUT": (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input"),
    "SUBMIT_BUTTON": (By.XPATH, "//button[normalize-space()='Зарегистрироваться']"),
}

# ---------- Страница аккаунта ----------
AccountPageLocators = {
    "LOGOUT_BUTTON": (By.XPATH, "//button[normalize-space()='Выход']"),
}

# ---------- Конструктор ----------
MainPageLocators = {
    "TAB_BUNS": (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Булки']]"),
    "TAB_SAUCES": (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Соусы']]"),
    "TAB_FILLINGS": (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Начинки']]"),
    "TAB_ACTIVE_TEXT": (By.XPATH, "//div[contains(@class,'tab') and contains(@class,'tab_type_current')]//span"),
}