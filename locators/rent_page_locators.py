from selenium.webdriver.common.by import By


class RentPageLocators:
    TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")
    WHERE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME = (By.CLASS_NAME, "Dropdown-arrow")
    BUTTON_NEXT = (By.XPATH, "//button[2][text()='Заказать']")
    ELEMENT_LIST = (By.XPATH, "//div[text()='сутки']")
    ELEMENT_LIST_2 = (By.XPATH, "//div[text()='двое суток']")
