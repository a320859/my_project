from selenium import webdriver
import pytest, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or es")
    

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('--language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':language})
    browser = webdriver.Chrome(options=options)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    yield browser
    browser.quit()

