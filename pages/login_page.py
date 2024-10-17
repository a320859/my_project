from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Подстроки login нет в урле!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет формы для логина!'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGIST_FORM), 'Нет формы для регистрации!'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGIST_EMAIL).send_keys(email) 
        self.browser.find_element(*LoginPageLocators.REGIST_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGIST_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGIST).click()