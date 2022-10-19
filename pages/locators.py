from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".add-to-basket .btn-add-to-basket")
    NAME_PRODUCT_LINK = (By.CSS_SELECTOR, ".product_page .product_main h1")
    STATUS_NAME_PRODUCT_LINK = (By.CSS_SELECTOR, ".alert:first-child strong")