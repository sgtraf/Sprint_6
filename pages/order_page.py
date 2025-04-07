import allure
from locators.order_page_locators import OrderPageLocators
from locators.rent_page_locators import RentPageLocators
from pages.base_page import BasePage
import data


# класс главной страницы
class OrderPageSamokat(BasePage):

    @allure.step("Подождать загрузки заголовка")
    def wait_for_title(self):
        self.wait_for_element(OrderPageLocators.TITLE)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Кликнуть на элемент кнопка как текст")
    def click_on_element_button(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, bandle):
        self.send_keys_to_input(OrderPageLocators.NAME, data.OrderData.order_data['Имя'][bandle])
        self.send_keys_to_input(OrderPageLocators.SURNAME, data.OrderData.order_data['Фамилия'][bandle])
        self.send_keys_to_input(OrderPageLocators.ADDRESS, data.OrderData.order_data['Адрес'][bandle])
        self.send_keys_to_input(OrderPageLocators.METRO, data.OrderData.order_data['Метро'][bandle])
        self.wait_for_element(OrderPageLocators.ELEMENT_LIST)
        self.click_on_element(OrderPageLocators.ELEMENT_LIST)
        self.send_keys_to_input(OrderPageLocators.PHONE, data.OrderData.order_data['Телефон'][bandle])

    @allure.step("Заполнить форму аренды")
    def fill_rent_form(self, bandle):
        self.send_keys_to_input(RentPageLocators.WHERE, data.OrderData.order_data['Дата'][bandle])
        self.click_on_element(RentPageLocators.TIME)
        self.click_on_element(RentPageLocators.ELEMENT_LIST)
