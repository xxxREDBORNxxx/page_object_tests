import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .tools_project import get_random_password, get_random_email

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    WAIT_TIME = 2

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

    def should_be_email_input_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LINK), "Email input-form is not presented"

    def should_be_password_1_input_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LINK_1), "password_1 input-form is not presented"

    def should_be_password_2_input_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LINK_2), "password_2 input-form is not presented"

    def should_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_LINK), "registration button is not presented"

    def should_click_registration_button(self):
        assert WebDriverWait(self.browser, self.WAIT_TIME).until(EC.element_to_be_clickable(
            LoginPageLocators.REGISTER_BUTTON_LINK))

    def should_be_active_register_input_form(self):
        self.should_be_email_input_form()
        self.should_be_password_1_input_form()
        self.should_be_password_2_input_form()
        self.should_click_registration_button()

    def input_email_in_registrations_form(self, email):
        self.browser.find_element(*LoginPageLocators.EMAIL_LINK).send_keys(email)

    def input_password_in_registrations_form_1(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_LINK_1).send_keys(password)

    def input_password_in_registrations_form_2(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_LINK_2).send_keys(password)

    def click_register(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_LINK).click()

    def register_new_user(self):

        email = get_random_email()
        password = get_random_password()

        print(f"generated email: {email}")
        print(f"generated password: {password}")

        self.input_email_in_registrations_form(email)
        self.input_password_in_registrations_form_1(password)
        self.input_password_in_registrations_form_2(password)
        self.click_register()
