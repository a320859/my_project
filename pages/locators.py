from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEAD_BUSKET_BUTTON = (By.CSS_SELECTOR, '.btn-group .btn')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGIST_FORM = (By.ID, 'register_form')

class ProductPageLocators:
    BUSKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BUSKET_TOTAL  = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert')
    
class BusketPagelocators:
    BUSKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BUSKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')