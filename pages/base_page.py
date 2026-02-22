from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url: str) -> None:
        self.driver.get(url)

webdriver