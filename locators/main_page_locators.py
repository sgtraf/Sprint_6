from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    @staticmethod
    def question_number(question):
        return By.ID, f'accordion__heading-{question}'
    @staticmethod
    def question_text(question):
        return By.ID, f'accordion__panel-{question}'