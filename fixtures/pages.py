from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_status_page import OrderStatusPage

import pytest


@pytest.fixture
def home_page(driver) -> HomePage:
    return HomePage(driver=driver)

@pytest.fixture
def order_page(driver) -> OrderPage:
    return OrderPage(driver=driver)

@pytest.fixture
def order_status_page(driver) -> OrderStatusPage:
    return OrderStatusPage(driver=driver)