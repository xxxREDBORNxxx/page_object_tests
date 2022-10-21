from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        """check for the correct url"""
        print(self.browser.current_url)
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/ru/basket/'

    def should_be_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_LINK), "Basket is not empty"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_LINK), \
            "Product is presented in basket, but should not be"
