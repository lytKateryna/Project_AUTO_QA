from selenium.webdriver.common.by import By
from My_HW.HW_6.pages.base import BasePage

class InventoryPage(BasePage):
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def add_to_cart(self):
        self.click_element(self.BACKPACK_BUTTON)
        self.click_element(self.TSHIRT_BUTTON)
        self.click_element(self.ONESIE_BUTTON)
        
    def open_cart(self):
        self.click_element(self.CART_BUTTON)

