from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def _login(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    return InventoryPage(driver)

def test_inventory_loads(driver):
    assert _login(driver).item_count() == 6

def test_add_to_cart(driver):
    inv = _login(driver)
    inv.add_first_to_cart()
    assert inv.cart_count() == "1"