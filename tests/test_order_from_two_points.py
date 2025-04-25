import allure
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.rent_page_locators import RentPageLocators
from locators.confirmation_page_locators import ConfirmationPageLocators
from locators.order_ok_page_locators import OrderOkPageLocators

class TestOrderFromTwoButtons:
    @allure.title("Тест заказа по нажатию на первую кнопку")
    def test_order_from_first_button(self, driver):
        # Arrange
        driver = driver
        #первый набор данных
        bandle = 0
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        order_page = OrderPageSamokat(driver)
        order_page.click_on_element(MainPageLocators.FIRST_ORDER_BUTTON)
        order_page.wait_for_title()
        # Assert
        order_page.fill_registration_form(bandle)
        #нажатие на кнопку
        order_page.click_on_element(OrderPageLocators.BUTTON_NEXT)
        order_page.fill_rent_form(bandle)
        #нажатие на кнопку
        order_page.click_on_element_button(RentPageLocators.BUTTON_NEXT)
        #нажатие на кнопку Да
        order_page.click_on_element(ConfirmationPageLocators.BUTTON_NEXT)
        assert order_page.get_text_on_element(OrderOkPageLocators.BUTTON) == 'Посмотреть статус'

    @allure.title("Тест заказа по нажатию на вторую кнопку")
    def test_order_from_second_button(self, driver):
        # Arrange
        driver = driver
        #второй набор данных
        bandle = 1
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        order_page = OrderPageSamokat(driver)
        order_page.click_on_element(MainPageLocators.FIRST_ORDER_BUTTON)
        order_page.wait_for_title()
        # Assert
        order_page.fill_registration_form(bandle)
        #нажатие на кнопку
        order_page.click_on_element(OrderPageLocators.BUTTON_NEXT)
        order_page.fill_rent_form(bandle)
        #нажатие на кнопку
        order_page.click_on_element_button(RentPageLocators.BUTTON_NEXT)
        #нажатие на кнопку Да
        order_page.click_on_element(ConfirmationPageLocators.BUTTON_NEXT)
        assert order_page.get_text_on_element(OrderOkPageLocators.BUTTON) == 'Посмотреть статус'
