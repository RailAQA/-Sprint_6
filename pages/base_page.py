from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url: str):
        self.driver.get(url)

    def get_locator(self, locator: tuple, nth: int = 0,):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)[nth]
    
    def click(self, locator: tuple, nth: int):
        element = self.get_locator(locator=locator, nth=nth)
        element.click()

    def check_visible(self, locator: str):
        element = self.get_locator(locator=locator)
        assert element.is_displayed()

    def check_have_text(self, locator: str, text: str, nth: int = 0):
        element = self.get_locator(locator=locator, nth=nth)     
        assert element.text == text

    def scroll_to(self, locator: str):
        #element = self.get_locator(locator=locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)