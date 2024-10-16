from .base_page import BasePage
from .locators import BasePageLocators, BusketPagelocators

class BusketPage(BasePage):
    def go_to_busket(self):
        self.browser.find_element(*BasePageLocators.HEAD_BUSKET_BUTTON).click()
    def should_be_empty_busket(self):
        assert self.browser.find_elements(*BusketPagelocators.BUSKET_ITEMS) == [], 'В корзине есть товары!!'
    def should_be_text_empty_busket(self):
        assert self.browser.find_elements(*BusketPagelocators.BUSKET_EMPTY_TEXT) != [], 'Текста в пустой корзине нет!'
        
