import pytest

from pages.home_page import HomePage
from tools.routes import AppRoute


class TestHomePage:
    @pytest.mark.parametrize("number", [i for i in range(0, 8)])
    def test_opening_drop_down_list(self, driver, number):
        home_page = HomePage(driver=driver)
        home_page.visit(AppRoute.HOME_PAGE)
        home_page.scroll_to_drop_down_list(nth=number)
        home_page.click_to_drop_down_list_value_button(nth=number)
        actual_option_text = home_page.get_actual_options_text(nth=number)
        expected_option_text = home_page.get_expected_options_text()[number]
        assert expected_option_text == actual_option_text