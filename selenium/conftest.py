import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    b = os.getenv("BROWSER","chrome").lower()
    if b == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(options=opts)
    else:
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless=new")
        driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
