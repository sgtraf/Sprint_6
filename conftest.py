import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data


@pytest.fixture
#открывает и закрывает вебдрайвер
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

