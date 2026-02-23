from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderStatusPage(BasePage):
    SAMOKAT_HEADER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')

    def click_samokat_header_logo(self):
        self.click(locator=self.SAMOKAT_HEADER_LOGO)