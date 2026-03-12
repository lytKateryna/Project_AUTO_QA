from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


BASE_URL = "https://itcareerhub.de/ru"


def test_find_logo(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')))
    assert logo.is_displayed()


def test_find_element_programm(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Программы')))
    assert element.is_displayed()


def test_find_element_praise(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Способы оплаты')))
    assert element.is_displayed()


def test_find_element_news(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Блог')))
    assert element.is_displayed()


def test_find_element_o_nas(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'О нас')))
    assert element.is_displayed()


def test_button(driver):
    driver.get(BASE_URL)
    button_sub = driver.find_element(By.CSS_SELECTOR, 'a[href="/ru"]')
    button_sub.click()

    assert BASE_URL in driver.current_url


def test_phone_icon_text(driver):
    wait = WebDriverWait(driver, 20)

    driver.get("https://itcareerhub.de/ru/contact-us")

    phone_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.tn-atom[href="#popup:form-tr"]'))
    )
    driver.execute_script("arguments[0].click();", phone_icon)

    expected_text = "Свяжемся с вами в течение 15 минут, чтобы назначить время консультации"

    popup_text = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "tn-group__1862496483175871291755985340"
                                          ))
    )

    assert expected_text in popup_text.text
