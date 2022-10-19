from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    WAIT_TIME = 5

    def check_click_basket(self):
        assert WebDriverWait(self.browser, self.WAIT_TIME).until(EC.element_to_be_clickable(
            ProductPageLocators.BASKET_LINK))

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()

    def get_product_title_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_LINK).text

    def get_product_name_in_message(self):
        return self.browser.find_element(*ProductPageLocators.STATUS_NAME_PRODUCT_LINK).text

    def compare_product_names(self):
        assert self.get_product_title_in_basket() == self.get_product_name_in_message(), \
            "Incorrect product name in the shopping cart message"
