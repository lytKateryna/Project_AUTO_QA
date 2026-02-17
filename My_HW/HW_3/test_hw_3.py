from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


def test_find_to_element(driver):
    driver.get("https://itcareerhub.de/ru")
    logo = driver.find_element(By.CSS_SELECTOR, 'img[src*="Group_3793.svg"]')
    assert logo.is_displayed()


def test_find_element_programm(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    element = driver.find_element(By.XPATH,
                                  "//*[contains(normalize-space(), 'Программы') or contains(normalize-space(), 'Programme')]")
    assert element.is_displayed()


def test_find_element_preise(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    element = driver.find_element(By.XPATH,
                                  "//*[contains(normalize-space(), 'Способы оплаты') or contains(normalize-space(), 'Preise')]")
    assert element.is_displayed()


def test_find_element(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    element = driver.find_element(By.XPATH,
                                  "//*[contains(normalize-space(), 'Новости')]")
    assert element.is_displayed()


def test_find_element_Über_uns(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    element = driver.find_element(By.XPATH,
                                  "//*[contains(normalize-space(), 'О нас') or contains(normalize-space(), 'Über_uns')]")
    assert element.is_displayed()


def test_find_element_Bewertungen(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    element = driver.find_element(By.XPATH,
                                  "//*[contains(normalize-space(), 'Отзывы') or contains(normalize-space(), 'Bewertungen')]")
    assert element.is_displayed()


def test_button(driver):
    driver.get("https://itcareerhub.de/ru")

    button_sub = driver.find_element(By.CSS_SELECTOR, 'a[href="/ru"]')
    button_sub.click()

    sleep(2)

    assert "https://itcareerhub.de/ru" in driver.current_url


def test_phone_icon_text(driver):
    wait = WebDriverWait(driver, 20)

    driver.get("https://itcareerhub.de/reviews")

    phone_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.tn-atom[href="#popup:form-tr3"]'))
    )
    driver.execute_script("arguments[0].click();", phone_icon)

    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"

    popup_text = wait.until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//div[contains(@class, 't-popup')]//*[contains(text(), 'Если вы не дозвонились, заполните форму')]"))
    )

    assert expected_text in popup_text.text
