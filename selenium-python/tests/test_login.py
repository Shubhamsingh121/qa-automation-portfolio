from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    assert InventoryPage(driver).title() == "Products"

def test_locked_out_user(driver):
    p = LoginPage(driver).open()
    p.login("locked_out_user", "secret_sauce")
    assert "locked out" in p.error().lower()

def test_invalid_password(driver):
    p = LoginPage(driver).open()
    p.login("standard_user", "wrong_pass")
    assert "do not match" in p.error()

def test_empty_credentials(driver):
    p = LoginPage(driver).open()
    p.login("", "")
    assert "Username is required" in p.error()