import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import Select

from locators.main_page_locators import MainPageLocators
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

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, bandle):
        self.send_keys_to_input(OrderPageLocators.NAME, data.OrderData.order_data['Имя'][bandle])
        self.send_keys_to_input(OrderPageLocators.SURNAME, data.OrderData.order_data['Фамилия'][bandle])
        self.send_keys_to_input(OrderPageLocators.ADDRESS, data.OrderData.order_data['Адрес'][bandle])
        self.send_keys_to_input(OrderPageLocators.METRO, data.OrderData.order_data['Метро'][bandle])
        self.wait_for_element(OrderPageLocators.ELEMENT_LIST)
        self.click_on_element(OrderPageLocators.ELEMENT_LIST)
        self.send_keys_to_input(OrderPageLocators.PHONE, data.OrderData.order_data['Телефон'][bandle])

    @allure.step("Открыть вопрос")
    def click_on_questions(self, questions_number):
        card_locator = MainPageLocators.question_number(questions_number)
        #print(card_locator)
        self.scroll_to_element(card_locator)
        self.click_on_element(card_locator)
