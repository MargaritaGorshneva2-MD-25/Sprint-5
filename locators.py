from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]") # Попробуйте уточнить локатор, если возможно
    # login_redirect_url - удалил, т.к. URL хранятся в URL.py

    # Вход/Личный кабинет
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_AREA_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # personal_area_page_url - удалил, т.к. URL хранятся в URL.py


    # Шапка
    LOGO_IMAGE = (By.CSS_SELECTOR, ".AppHeader_header__logo")

    # Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    # Формы входа/регистрации/восстановления пароля
    LOGIN_LINK_REGISTRATION = (By.LINK_TEXT, "Войти")
    LOGIN_LINK_FORGOT_PASSWORD = (By.LINK_TEXT, "Войти") # Убедитесь, что это корректный локатор
    # login_page_url - удалил, т.к. URL хранятся в URL.py

    # Ингредиенты
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    @staticmethod
    def get_section_locator(tab_name):
        # Используем CSS селекторы и data-атрибуты, если доступны
        if tab_name == "Булки":
            return (By.CSS_SELECTOR, "[data-tab='bun']")
        elif tab_name == "Соусы":
            return (By.CSS_SELECTOR, "[data-tab='sauce']")
        elif tab_name == "Начинки":
            return (By.CSS_SELECTOR, "[data-tab='main']")
        else:
            raise ValueError(f"Неправильное имя вкладки: {tab_name}")

