from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_IMAGE = (By.XPATH, "//div[@class='profile__image']")
    AVATAR_INPUT = (By.ID, "owner-avatar")
    UPDATE_AVATAR_BUTTON = (By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']")
    CARDS = (By.CLASS_NAME, "card__image")
    CARD_NAME_IN_POPUP = (By.CLASS_NAME, "popup__caption")

    @staticmethod
    def question_number(question):
        return By.ID, f'//div[@id="accordion__panel-{question}"]]'