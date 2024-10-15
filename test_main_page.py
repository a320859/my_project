from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(url='http://selenium1py.pythonanywhere.com/', browser=browser)
    page.open()
    page.go_to_login_page()
