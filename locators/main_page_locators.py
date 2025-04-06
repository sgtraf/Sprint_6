from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SAMOKAT_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    @staticmethod
    def question_number(question):
        return By.ID, f'accordion__heading-{question}'
    @staticmethod
    def question_text(question):
        return By.ID, f'accordion__panel-{question}'