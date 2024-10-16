from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON).click()
    def title_should_be_like_message(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE).text  
        message = self.browser.find_element(*ProductPageLocators.MESSAGE).text  
        assert title == message, 'Название товара и добавленный в корзину товар не совпадают!'
    def price_should_be_like_busket_total(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        busket_total = self.browser.find_element(*ProductPageLocators.BUSKET_TOTAL).text
        assert price == busket_total, 'Цена не равна значению в корзине!'
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Сообщение есть, хотя его не должно быть!"
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Сообщения нет, хотя оно должно быть!"
    def should_not_be_success_message_disp(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Сообщения об успехе нет! disp'