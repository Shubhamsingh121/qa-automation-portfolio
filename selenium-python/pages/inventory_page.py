from selenium.webdriver.common.by import By

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_BTNS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.find_element(*self.TITLE).text

    def item_count(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def add_first_to_cart(self):
        self.driver.find_elements(*self.ADD_BTNS)[0].click()

    def cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text