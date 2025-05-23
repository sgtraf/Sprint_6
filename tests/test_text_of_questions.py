import allure
import pytest
import data
from pages.main_page import MainPageSamokat


class TestCardNames:
    @allure.title("Тест текста ответов на вопросы")
    @pytest.mark.parametrize('questions_number, expected_text', data.Data.questions_names)
    def test_card_names(self, driver, questions_number, expected_text):
        # Arrange
        driver = driver
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        main_page.click_on_questions(questions_number)
        # Assert
        assert main_page.check_questions_name(questions_number, expected_text)
