from selenium.webdriver.common.by import By
from My_HW.HW_6.pages.base import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def checkout(self, first_name, last_name, zip_code):
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.ZIP_CODE_INPUT, zip_code)




    def continue_to_checkout(self):
        self.click_element(self.CONTINUE_BUTTON)