import allure
import curl
from pages.main_page import MainPageSamokat
from locators.main_page_locators import MainPageLocators


class TestRedirectFromButtons:
    @allure.title("Тест редиректа с нажатия на кнопку Яндекс ")
    def test_yandex_button(self, driver):
        # Arrange
        driver = driver
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        main_page.click_on_element(MainPageLocators.YANDEX_BUTTON)
        main_page.switch_to_next_tab()
        main_page.wait_for_element(MainPageLocators.DZEN_SEARCH)
        # Assert
        assert driver.current_url == curl.DZEN_URL

    @allure.title("Тест редиректа с нажатия на кнопку Самокат ")
    def test_samokat_button(self, driver):
        # Arrange
        driver = driver
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        #Предвариительно переходим на другую страницу
        driver.get(curl.MAIN_URL + curl.ORDER_URL)
        # Клик на кнопку самоката
        main_page.click_on_element(MainPageLocators.SAMOKAT_BUTTON)
        main_page.wait_for_questions_list()
        # Assert
        assert driver.current_url == curl.MAIN_URL
