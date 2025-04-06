import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from curl import *


@pytest.fixture
#открывает и закрывает вебдрайвер
def driver():
    browser = webdriver.Firefox()
    browser.get(main_site)
    yield browser
    browser.quit()

