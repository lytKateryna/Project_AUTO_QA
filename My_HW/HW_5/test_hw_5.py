from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

BASE_URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"


def test_iframe(driver):
    driver.get(BASE_URL)

    driver.switch_to.frame("my-iframe")

    element = driver.find_element(By.TAG_NAME, "body")

    assert "semper posuere integer et senectus justo curabitur." in element.text


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 15)

    buttons = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )

    for button in buttons:
        if button.text.strip() == "Einwilligen":
            button.click()
            break

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame")))

    photos_before = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li"))
    )
    assert len(photos_before) == 4

    source = photos_before[0]
    trash = driver.find_element(By.ID, "trash")

    ActionChains(driver).click_and_hold(source).move_to_element(trash).release().perform()

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3)

    photos_in_trash = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    photos_in_gallery = driver.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(photos_in_trash) == 1
    assert len(photos_in_gallery) == 3