import pytest
import allure

from pages.home_page import HomePage
from tools.fakers import faker
from pages.order_page import OrderPage
from tools.routes import AppRoute


class TestOrderPage:
    @allure.title("Флоу успешный заказ самоката")
    @pytest.mark.parametrize("index", [i for i in range(0, 2)])
    def test_succesful_order_flow(self, driver, index):
        home_page = HomePage(driver=driver)
        home_page.visit(AppRoute.HOME_PAGE)
        home_page.click_order_button(nth=index)

        order_page = OrderPage(driver=driver)
        order_page.fill_samokat_form(
            name=faker.name(), 
            last_name=faker.last_name(),
            address=faker.address(),
            phone=faker.phone_nubmer()
            )
        order_page.click_next_button()
        order_page.fill_rent_form(
            date=faker.date(), 
            comment=faker.sentence(), 
            nth=index
            )
        order_page.click_make_order()
        order_page.click_approve_order_button()
        order_page.check_visible_succesful_order_form()

    @allure.title("Переход на главную страницу через логотип Самоката")
    def test_samokat_logo_navigation(self, driver):
        order_page = OrderPage(driver=driver)
        order_page.visit(AppRoute.ORDER_PAGE)
        order_page.click_samokat_header_logo()
        order_page.check_current_url(url=AppRoute.HOME_PAGE)

    @allure.title("Переход на главную страницу Дзена через логотип Яндекса")
    def test_yandex_logo_navigation(self, driver):
        home_page = HomePage(driver=driver)
        home_page.visit(AppRoute.HOME_PAGE)
        home_page.click_yandex_header_logo()
        home_page.swith_to_next_tab()
        home_page.check_current_url(url="https://dzen.ru/?yredirect=true")