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

    # Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    # Формы входа/регистрации/восстановления пароля
    LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//a[@href='/login']")
    LOGIN_LINK_FORGOT_PASSWORD_FORM = (By.XPATH, "//a[@href='/forgot-password']")

    # Ингредиенты
    BUNS_TAB = (By.CSS_SELECTOR, "[data-tab='bun']")
    SAUCES_TAB = (By.CSS_SELECTOR, "[data-tab='sauce']")
    FILLINGS_TAB = (By.CSS_SELECTOR, "[data-tab='main']")

    # Секции ингредиентов (для проверки скролла)
    @staticmethod
    def get_section_locator(tab_name):
        if tab_name == "Булки":
            return (By.CSS_SELECTOR, "[data-section='bun']")
        elif tab_name == "Соусы":
            return (By.CSS_SELECTOR, "[data-section='sauce']")
        elif tab_name == "Начинки":
            return (By.CSS_SELECTOR, "[data-section='main']")
        else:
            raise ValueError(f"Неизвестное название вкладки: {tab_name}")

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
