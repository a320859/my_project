from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BusketPage
import time, pytest
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(link, browser)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", '6789se6789se') 
        page.should_be_authorized_user() 

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(link, browser)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.title_should_be_like_message()
        page.price_should_be_like_busket_total()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(link,browser)    
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket( browser):
        page = ProductPage(link, browser)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.title_should_be_like_message()
        page.price_should_be_like_busket_total()

def test_guest_cant_see_success_message(browser):
        page = ProductPage(link,browser)    
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail() 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(link,browser)    
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    

@pytest.mark.xfail() 
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(link,browser)    
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_disp()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(link, browser)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(link, browser)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
    page = BusketPage(link, browser)
    page.open()
    page.go_to_busket()
    page.should_be_empty_busket()
    page.should_be_text_empty_busket()