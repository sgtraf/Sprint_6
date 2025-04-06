import allure
import pytest
import curl
from pages.main_page import MainPageSamokat
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class TestOrderFromTwoButtons:
    @allure.title("Тест заказа по нажатию на первую кнопку")
    def test_order_from_first_button(self, driver):
        # Arrange
        driver = driver
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        main_page.click_on_element(MainPageLocators.FIRST_ORDER_BUTTON)
        main_page.wait_for_element(OrderPageLocators.TITLE)
        # Assert
        assert driver.current_url == curl.ORDER_URL

    @allure.title("Тест заказа по нажатию на вторую кнопку")
    def test_order_from_second_button(self, driver):
        # Arrange
        driver = driver
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        #Предвариительн переходим на другую страницу
        main_page.scroll_to_element(MainPageLocators.SECOND_ORDER_BUTTON)
        main_page.click_on_element(MainPageLocators.SECOND_ORDER_BUTTON)
        main_page.wait_for_element(OrderPageLocators.TITLE)
        # Assert
        assert driver.current_url == curl.ORDER_URL