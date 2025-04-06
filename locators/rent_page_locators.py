from selenium.webdriver.common.by import By


class RentPageLocators:
    TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")
    WHERE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME = (By.CLASS_NAME, "Dropdown-placeholder")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Заказать']")
    ELEMENT_LIST = (By.XPATH, "//li[@class='select-search__row']")