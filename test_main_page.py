from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BusketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(link, browser )
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser.current_url, browser)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(link, browser )
        page.open()
        page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BusketPage(link, browser)
    page.open()
    page.go_to_busket()
    page.should_be_empty_busket()
    page.should_be_text_empty_busket()