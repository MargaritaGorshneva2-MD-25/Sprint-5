from selenium.webdriver.common.by import By

base_url = "https://stellarburgers.nomoreparties.site/"

class Locators:
    # Регистрация
    name_field = (By.NAME, "name")
    email_field = (By.NAME, "email")
    password_field = (By.CSS_SELECTOR, "input[name='Пароль']") # CSS selector, так как name содержит кириллицу
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    error_message_locator = (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]") # Нужно уточнить, если есть id у сообщения
    login_redirect_url = (base_url + "login")

    # Вход/Личный кабинет
    login_button_main_page = (By.XPATH, "//button[text()='Войти в аккаунт']") # Уточненный текст
    personal_area_button = (By.CSS_SELECTOR, "a[href='/account']") # CSS selector по атрибуту href
    login_button = (By.XPATH, "//button[text()='Войти']")
    personal_area_page_url = (base_url + "account/profile")

    # Шапка
    logo_image = (By.CSS_SELECTOR, ".AppHeader_header__logo") # CSS selector для логотипа

    # Выход
    logout_button = (By.XPATH, "//button[text()='Выйти']")


    # Формы входа/регистрации/восстановления пароля
    login_link_registration = (By.LINK_TEXT, "Войти") # Link Text для ссылки "Войти" на странице регистрации
    login_link_forgot_password = (By.LINK_TEXT, "Войти") # Link Text для ссылки "Войти" на странице восстановления пароля
    login_page_url = (base_url + "login")


    # Ингредиенты
    buns_tab = (By.XPATH, "//span[text()='Булки']") # Уточненный XPath
    sauces_tab = (By.XPATH, "//span[text()='Соусы']") # Уточненный XPath
    fillings_tab = (By.XPATH, "//span[text()='Начинки']") # Уточненный XPath

    @staticmethod
    def get_section_locator(tab_name):
        # Используем CSS селекторы и data-атрибуты (если доступны)
        if tab_name == "Булки":
            return (By.CSS_SELECTOR, "[data-tab='bun']")
        elif tab_name == "Соусы":
            return (By.CSS_SELECTOR, "[data-tab='sauce']")
        elif tab_name == "Начинки":
            return (By.CSS_SELECTOR, "[data-tab='main']")
        else:
            raise ValueError(f"Неправильное имя вкладки: {tab_name}")
