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
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
