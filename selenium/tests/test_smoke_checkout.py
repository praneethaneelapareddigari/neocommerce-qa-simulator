from selenium.utils import config
from selenium.pages.home_page import HomePage

def test_home_smoke(browser):
    hp = HomePage(browser)
    hp.open(config.BASE_URL)
    assert browser.title != ''
