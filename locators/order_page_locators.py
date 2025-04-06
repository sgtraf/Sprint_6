from selenium.webdriver.common.by import By


class OrderPageLocators:
    TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")

    QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SAMOKAT_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    DZEN_SEARCH = (By.CLASS_NAME, "xa2987efd")
    FIRST_ORDER_BUTTON = "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"