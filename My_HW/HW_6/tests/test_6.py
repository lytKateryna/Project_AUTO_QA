from My_HW.HW_6.pages.checkout_total import CheckoutTotal
from My_HW.HW_6.pages.login_page import Login_Page
from My_HW.HW_6.pages.inventory_page import InventoryPage
from My_HW.HW_6.pages.cart_page import CartPage
from My_HW.HW_6.pages.checkout_page import CheckoutPage
from My_HW.HW_6.conf_test import driver


def test_check_total(driver):
    login_page = Login_Page(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_total = CheckoutTotal(driver)

    login_page.open(driver)
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart()
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.checkout("John", "Doe", "12345")
    checkout_page.continue_to_checkout()
    total_price = checkout_total.get_total_price()
    assert total_price == 58.29

