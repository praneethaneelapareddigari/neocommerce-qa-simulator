from selenium.webdriver.common.by import By
def by_css(selector:str):
    return (By.CSS_SELECTOR, selector)
