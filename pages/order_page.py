from pages.base_page import BasePage

import allure
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    UNDERGROUND_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    DROP_DOWN_OPTIONS = (By.XPATH, '//li[@class="select-search__row"]')

    DATE_OF_DELIVERY_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_DROP_DOWN = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENTAL_PERIOD_OPTIONS = (By.XPATH, '//div[@class="Dropdown-option"]')
    SAMOKAT_COLOR_CHECKBOXES = (By.XPATH, '//input[@class="Checkbox_Input__14A2w"]')
    CURRIER_COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    APPROVE_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESFUL_ORDER_FORM_TITTLE = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    CHECK_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    @allure.step("Заполнение формы с пользовательскими данными самоката")
    def fill_samokat_form(self, name: str, last_name: str, address: str, phone: str):
        self.hide_cookie_banner()
        self.fill(locator=self.NAME_INPUT, text=name)
        self.fill(locator=self.LAST_NAME_INPUT, text=last_name)
        self.fill(locator=self.ADDRESS_INPUT, text=address)
        self.choice_metro()
        self.fill(locator=self.PHONE_NUMBER_INPUT, text=phone)
        
    @allure.step("Клик по кнопке 'Далее' в форме с пользовательскими данными самоката")
    def click_next_button(self):
        self.click(locator=self.NEXT_BUTTON)

    @allure.step("Заполнение формы аренды самоката")
    def fill_rent_form(self, date: str, comment: str, nth):
        self.fill(locator=self.DATE_OF_DELIVERY_INPUT, text=date)
        self.driver.find_element(*self.DATE_OF_DELIVERY_INPUT).send_keys(Keys.ENTER)
        self.choice_rental_period()
        self.click(locator=self.SAMOKAT_COLOR_CHECKBOXES, nth=nth)
        self.fill(locator=self.CURRIER_COMMENT_INPUT, text=comment)

    @allure.step("Кнопка 'Сделать заказ' в форме аренды самоката")
    def click_make_order(self):
        self.click(locator=self.MAKE_ORDER_BUTTON)

    @allure.step("Выбор рандомного метро")
    def choice_metro(self):
        element = self.get_locator(locator=self.UNDERGROUND_STATION_INPUT)
        element.click()
        self.wait_element_will_visible(locator=self.DROP_DOWN_OPTIONS, timeout=5)
        
        options = self.driver.find_elements(*self.DROP_DOWN_OPTIONS)
        undeground = random.choice(options)
        self.scroll_to(locator=element)
        undeground.click()

    @allure.step("Выбор рандомного срока аренды")
    def choice_rental_period(self):
        element = self.get_locator(locator=self.RENTAL_PERIOD_DROP_DOWN)
        element.click()
        self.wait_element_will_visible(locator=self.RENTAL_PERIOD_OPTIONS, timeout=5)

        options = self.driver.find_elements(*self.RENTAL_PERIOD_OPTIONS)
        rental_period = random.choice(options)
        self.scroll_to_center(locator=rental_period)
        rental_period.click()

    def hide_cookie_banner(self):
        with allure.step(
            f"Скрытие баннера с куки"
            ):
            self.driver.execute_script("""
                var button = document.getElementById('rcc-confirm-button');
            if(button) {
                button.click();}
            """)

    @allure.step("Проверка, что отобразилось окно успешного заказа")
    def check_visible_succesful_order_form(self):
        self.check_visible(locator=self.SUCCESFUL_ORDER_FORM_TITTLE)
        self.check_visible(locator=self.CHECK_STATUS_BUTTON)

    @allure.step("Клик по кнопке 'Проверить статус заказа'")
    def click_check_status_button(self):
        self.click(locator=self.CHECK_STATUS_BUTTON)

    @allure.step("Клик по кнопке 'Да' в форме аренды")
    def click_approve_order_button(self):
        self.click(locator=self.APPROVE_ORDER_BUTTON)