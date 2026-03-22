from selenium.webdriver.common.by import By
from My_HW.HW_6.pages.base import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)