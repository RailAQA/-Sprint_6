from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):
    DROP_DOWN_LIST_VALUE_BUTTONS = (By.XPATH, "//div[@data-accordion-component='AccordionItemHeading']")
    DROP_DOWN_LIST_OPTIONS = (By.XPATH, '//div[@data-accordion-component="AccordionItemPanel"]//p')

    ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    YANDEX_HEADER_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')

    @allure.step("Скролл к выпадающему списку")
    def scroll_to_drop_down_list(self, nth: int):
        self.hide_scooter_image()
        element = self.get_locator(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, nth=nth)
        self.scroll_to(locator=element)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DROP_DOWN_LIST_VALUE_BUTTONS))

    def click_to_drop_down_list_value_button(self, nth: int):
        self.click(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, nth=nth)

    def get_actual_options_text(self, nth: int) -> str:
        element = self.driver.find_elements(*self.DROP_DOWN_LIST_OPTIONS)
        with allure.step(
            f"Получение фактического текста пунка выпадающего списка с локатором {self.DROP_DOWN_LIST_OPTIONS} с индексом {nth}"
            ):
            return element[nth].text

    def get_expected_options_text(self) -> str:
        data = []
        element = self.driver.find_elements(*self.DROP_DOWN_LIST_OPTIONS)
        with allure.step(
            f"Получение фактического текста пунка выпадающего списка с локатором {self.DROP_DOWN_LIST_OPTIONS}"
            ):
            for i in range(len(element)):
                data.append(element[i].text)
            return data

    def click_order_button(self, nth: int):
        self.hide_scooter_image()
        element = self.get_locator(locator=self.ORDER_BUTTON, nth=nth)
        self.scroll_to_center(locator=element)
        
        self.click(locator=self.ORDER_BUTTON, nth=nth)

    def click_yandex_header_logo(self):
        self.click(locator=self.YANDEX_HEADER_LOGO)

    def swith_to_next_tab(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

        WebDriverWait(self.driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(self.driver, 10).until(
    EC.url_to_be("https://dzen.ru/?yredirect=true")
)