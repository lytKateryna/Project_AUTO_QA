
from selenium.webdriver.common.by import By
from My_HW.HW_6.pages.base import BasePage

class Login_Page(BasePage):
    URL = "https://www.saucedemo.com/"
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


    def open(self, driver):
        driver.get(self.URL)

    def login(self, username, password):
        self.input_text(self.USER_NAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)


