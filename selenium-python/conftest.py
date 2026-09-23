import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    d = webdriver.Chrome(options=opts)
    d.implicitly_wait(5)
    yield d
    d.quit()