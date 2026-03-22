import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# def test_file_upload(browser):
#     browser.get("https://the-internet.herokuapp.com/upload")
#     upload = browser.find_element(By.ID, "file-upload")
#     upload.send_keys("E:\\Work\\autoqa\\lesson5\key.jpg")
#
#     button_upload = browser.find_element(By.ID, "file-submit")
#     button_upload.click()

    # sleep(5)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def test_troll_panel(driver):
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    panel = driver.find_element(By.CLASS_NAME, "trollface")
    panel.click()
    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)
    x_value = driver.find_element(By.ID, "input_value").text
    result = calc(x_value)
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()
    sleep(5)333333333333333333333333333333333