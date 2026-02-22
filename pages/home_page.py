from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    DROP_DOWN_LIST_VALUE_BUTTONS = (By.XPATH, "//div[@data-accordion-component='AccordionItemHeading']")
    DROP_DOWN_LIST_OPTIONS = (By.XPATH, '//div[@data-accordion-component="AccordionItemPanel"]//p')

    def scroll_to_drop_down_list(self, nth: int):
        self.hide_scooter_image()
        element = self.get_locator(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, nth=nth)
        self.scroll_to(locator=element)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DROP_DOWN_LIST_VALUE_BUTTONS))

    def click_to_drop_down_list_value_button(self, nth: int):
        self.click(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, nth=nth)

    def get_actual_options_text(self, nth: int) -> str:
        element = self.driver.find_elements(*self.DROP_DOWN_LIST_OPTIONS)
        return element[nth].text

    def get_expected_options_text(self) -> str:
        data = []
        element = self.driver.find_elements(*self.DROP_DOWN_LIST_OPTIONS)
        for i in range(len(element)):
            data.append(element[i].text)
        return data

    def hide_scooter_image(self):
        self.driver.execute_script("""
        var scooter = document.querySelector('div.Home_Scooter__3YdJy, div[class*="Home_Scooter"]');
        if(scooter) scooter.style.display = 'none';
        
        var blueprint = document.querySelector('div.Home_BluePrint__TGX2n, div[class*="Home_BluePrint"]');
        if(blueprint) blueprint.style.display = 'none';
    """)