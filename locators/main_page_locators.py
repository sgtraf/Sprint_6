from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SAMOKAT_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    DZEN_SEARCH = (By.CLASS_NAME, "xa2987efd")
    FIRST_ORDER_BUTTON = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    SECOND_ORDER_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")


    @staticmethod
    def question_number(question):
        return By.ID, f'accordion__heading-{question}'

    @staticmethod
    def question_text(question):
        return By.ID, f'accordion__panel-{question}'