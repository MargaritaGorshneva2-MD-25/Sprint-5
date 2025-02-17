from selenium.webdriver.common.by import  By


class Locators:
    # Локаторы для регистрации
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//div/main/section[2]/div/button[text()='Войти в аккаунт']") # Кнопка Войти в аккаунт
    REG_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Плейсхолдер Имя
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Плейсхолдер Email
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Плейсхолдер Пароль
    REGISTER_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']") # Кнопка подтверждения регистрации
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[text()='Войти']") # Кнопка Войти
    ERROR_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение об ошибке

    # Локаторы для входа по кнопке "Войти в аккаунт"
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//div/main/section[2]/div/button[text()='Войти в аккаунт']") # Кнопка Войти в аккаунт
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка Оформит заказ

    # Локаторы для входа по кнопке "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка Личный кабинет

    # Локаторы для входа по кнопке в форме регистрации
    LINK_LOGIN = (By.XPATH, "//a[starts-with(@ href,'/login')]")

    # Локаторы для входа по кнопке в форме восстановления пароля
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[starts-with(@ href,'/forgot-password')]")

    # Локатор перехода в Личный кабинет
    PROFILE = (By.XPATH, "//a[starts-with(@ href,'/account/profile')]")

    # Локатор перехода из Личного кабинета в Конструктор
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # Локатор перехода в Конструктор по Логотипу
    LOGO = (By.XPATH, "//a[starts-with(@ href,'/')]")

    # Локатор для выхода
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Локатор для перехода к соусам
    SAUCES_BUTTON = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Соусы']") # Кнопка Соусы
    SAUCES_MENU = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text()='Соусы']") # Меню Соусы

    # Локатор для перехода к начинкам
    FILLINGS_BUTTON = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Начинки']")  # Кнопка Начинки
    FILLINGS_MENU = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text()='Начинки']")  # Меню Начинки

    # Локатор для перехода к булкам
    BUNS_BUTTON = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Булки']")  # Кнопка Булки
    BUNS_MENU = (By.XPATH,"//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text()='Булки']")  # Меню Булки

    # Локатор для раздела конструктор
    ACTIVE_DIV_IN_CONSTRUCTOR = By.XPATH, './/div[contains(@class, "current")]/span'