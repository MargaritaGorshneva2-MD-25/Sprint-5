from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Вход/Личный кабинет
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PERSONAL_AREA_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Шапка
    LOGO_IMAGE = (By.CSS_SELECTOR, ".AppHeader_header__logo")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/' and contains(text(), 'Конструктор')]")

    # Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    # Формы входа/регистрации/восстановления пароля
    LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//a[@href='/login']")
    LOGIN_LINK_FORGOT_PASSWORD_FORM = (By.XPATH, "//a[@href='/forgot-password']")
    LOGIN_LINK_FORGOT_PASSWORD_FORM_2 = (By.XPATH, "//a[@href='/login']")


    # Ингредиенты
    BUNS_TAB = (By.CSS_SELECTOR, "[data-tab='bun']")
    SAUCES_TAB = (By.CSS_SELECTOR, "[data-tab='sauce']")
    FILLINGS_TAB = (By.CSS_SELECTOR, "[data-tab='main']")

    # Секции ингредиентов
    BUNS_SECTION = (By.CSS_SELECTOR, "[data-section='bun']")
    SAUCES_SECTION = (By.CSS_SELECTOR, "[data-section='sauce']")
    FILLINGS_SECTION = (By.CSS_SELECTOR, "[data-section='main']")

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
