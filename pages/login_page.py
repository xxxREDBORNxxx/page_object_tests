from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """check for the correct url"""
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_form(self):
        """check the presence of the login form"""
        print(self.browser.current_url)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """check the availability of the registration form on the page"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
