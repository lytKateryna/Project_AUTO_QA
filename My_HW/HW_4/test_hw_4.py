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


def test_text_input(driver):
    driver.get('http://uitestingplayground.com/textinput')
    wait = WebDriverWait(driver, 10)
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))
    assert driver.find_element(By.ID, "updatingButton").text == "ITCH"


def test_text_images(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 20)

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4)

    images = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
    )
    image3_alt = images[2].get_attribute("alt")
    assert image3_alt == "award"