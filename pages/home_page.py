from pages.base_page import BasePage
from data.faq_data import get_faq_data

from selenium.webdriver.common.by import By
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
        self.scroll_to_center(locator=element)
        self.wait_element_will_visible(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, timeout=5)

    @allure.step("Клик по контейнеру выпадающего списка")
    def click_to_drop_down_list_value_button(self, nth: int):
        self.click(locator=self.DROP_DOWN_LIST_VALUE_BUTTONS, nth=nth)

    def get_actual_options_text(self, nth: int) -> str:
        element = self.driver.find_elements(*self.DROP_DOWN_LIST_OPTIONS)
        with allure.step(
            f"Получение фактического текста пункта выпадающего списка с локатором {self.DROP_DOWN_LIST_OPTIONS} с индексом {nth}"
            ):
            return element[nth].text

    def get_expected_options_text(self, nth: int) -> str:
        data = get_faq_data()
        with allure.step(
            f"Получение ожидаемого текста пункта выпадающего списка с локатором {self.DROP_DOWN_LIST_OPTIONS}"
            ):
            return data[nth]

    @allure.step("Клик по кнопке сделать заказ")
    def click_order_button(self, nth: int):
        self.hide_scooter_image()
        element = self.get_locator(locator=self.ORDER_BUTTON, nth=nth)
        self.scroll_to_center(locator=element)
        
        self.click(locator=self.ORDER_BUTTON, nth=nth)

    @allure.step("Клик по логотипу 'Яндекс' в шапке")
    def click_yandex_header_logo(self):
        self.click(locator=self.YANDEX_HEADER_LOGO)

    @allure.step("Переход на другую вкладку")
    def swith_to_next_tab(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

        self.wait_url_to_be(timeout=5, url="https://dzen.ru/?yredirect=true")

    