import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    _driver = webdriver.Firefox(service=service)
    _driver.maximize_window()
    yield _driver
    _driver.quit()


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    time.sleep(1)
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    time.sleep(1)
    driver.save_screenshot("./My_HW/HW_2/payment screen.png")
    time.sleep(1)