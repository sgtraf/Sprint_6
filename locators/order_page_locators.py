from selenium.webdriver.common.by import By


class OrderPageLocators:
    TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")
    ELEMENT_LIST = (By.XPATH, "//li[@class='select-search__row']")
