from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс главной страницы
class MainPageSamokat:
    QUESTION_LOCATORS = [(By.ID, 'accordion__heading-0'), (By.ID, 'accordion__heading-1'),
                         (By.ID, 'accordion__heading-2'), (By.ID, 'accordion__heading-3'),
                         (By.ID, 'accordion__heading-4'), (By.ID, 'accordion__heading-5'),
                         (By.ID, 'accordion__heading-6'), (By.ID, 'accordion__heading-7') ]

    TEXT_QUESTION_LOC = [(By.ID, 'accordion__panel-0'), (By.ID, 'accordion__panel-1'),
                         (By.ID, 'accordion__panel-2'), (By.ID, 'accordion__panel-3'),
                         (By.ID, 'accordion__panel-4'), (By.ID, 'accordion__panel-5'),
                         (By.ID, 'accordion__panel-6'), (By.ID, 'accordion__panel-7')]

    password_field = [By.ID, 'password']
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

# класс главной страницы
class HomePageMesto:
    # создай локатор для поля «Занятие» в профиле пользователя
    profile_description = [By.CLASS_NAME, 'profile__description']

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы
    # ожидаем появление поля «Занятие»
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.profile_description))

    # метод для получения значения поля «Занятие»
    def get_description(self):
        return self.driver.find_element(*self.profile_description).text

class TestPraktikum:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_get_description(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-mesto.praktikum-services.ru/')

        # создай объект класса страницы авторизации
        login_page = LoginPageMesto(self.driver)
        # выполни авторизацию
        login_page.login('email учётной записи', 'пароль учётной записи')

        # создай объект класса главной страницы приложения
        home_page = HomePageMesto(self.driver)
        # дождись загрузки главной страницы
        home_page.wait_for_load_home_page()
        # сохрани в переменную description значение поля «Занятие»
        description = home_page.get_description()

        # проверь через assert, что полученное текстовое значение поля «Занятие» совпадает с ожидаемым
        assert description == 'занятие пользователя для твоей учетной записи'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()