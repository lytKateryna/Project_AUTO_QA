from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    # Locators
    NAME_FIELD = (By.ID, "name")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationintesting.online/"

    def open(self):
        self.driver.get(self.url)


