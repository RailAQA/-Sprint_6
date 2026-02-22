import pytest

from pages.home_page import HomePage


@pytest.mark.parametrize("number", [i for i in range(0, 8)])
def test_opening_drop_down_list(driver, number):
    home_page = HomePage(driver=driver)
    home_page.visit("https://qa-scooter.praktikum-services.ru")
    home_page.scroll_to_drop_down_list(nth=number)
    home_page.click_to_drop_down_list_value_button(nth=number)
    assert home_page.get_expected_options_text()[number] == home_page.get_actual_options_text(nth=number)