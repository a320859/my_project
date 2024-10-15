from selenium.webdriver.common.by import By
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    REGIST_FORM = (By.ID, 'register_form')
    REGIST_EMAIL = (By.ID, 'id_registration-email')
    REGIST_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGIST_PASSWORD2 = (By.ID, 'id_registration-password2')
    