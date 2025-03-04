from selenium.webdriver.common.by import By


class Locators:
    # Форма авторизации/регистрации
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    REG_BUTTON = (By.LINK_TEXT, "Зарегистрироваться")
    NAME = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']") # Можно использовать type='password' если атрибут name отсутствует
    REGISTER_BUTTON = (By.XPATH, "//form//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[contains(text(),'Войти')]")
    ERROR_TEXT = (By.XPATH, "//p[contains(text(),'Некорректный')]")

    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Разделы сайта (Личный кабинет, Конструктор)
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    LINK_LOGIN = (By.XPATH, "//a[contains(@href,'/login')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
    PROFILE = (By.XPATH, "//a[contains(@href,'/account/profile')]")
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    LOGO = (By.XPATH, "//a[contains(@href,'/')]")

    # Кнопка выхода
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    # Ингредиенты бургера
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    SAUCES_MENU = (By.XPATH, "//h2[contains(text(),'Соусы')]") #
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")
    FILLINGS_MENU = (By.XPATH, "//h2[contains(text(),'Начинки')]")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")
    BUNS_MENU = (By.XPATH, "//h2[contains(text(),'Булки')]")

    # Активный раздел в конструкторе
    ACTIVE_DIV_IN_CONSTRUCTOR = (By.XPATH, ".//div[contains(@class, 'current')]/span")


