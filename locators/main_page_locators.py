from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def question_number(question):
        return By.ID, f'//div[@id="accordion__panel-{question}"]]'