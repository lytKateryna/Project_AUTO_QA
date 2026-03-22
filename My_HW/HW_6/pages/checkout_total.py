from selenium.webdriver.common.by import By
from My_HW.HW_6.pages.base import BasePage
from My_HW.HW_6.pages.inventory_page import InventoryPage

class CheckoutTotal(BasePage):
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def get_total_price(self):
        total_price = self.get_text(self.TOTAL_LABEL)
        return float(total_price.replace("Total: $", ""))

