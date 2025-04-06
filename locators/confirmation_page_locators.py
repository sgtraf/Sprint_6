from selenium.webdriver.common.by import By


class ConfirmationPageLocators:
    TITLE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Да']")
