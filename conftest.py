import pytest
from selenium import webdriver
from curl import *


@pytest.fixture
#открывает и закрывает вебдрайвер
def driver():
    browser = webdriver.Firefox()
    browser.get(MAIN_URL)
    yield browser
    browser.quit()
