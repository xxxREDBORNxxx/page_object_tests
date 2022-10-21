from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOOK_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")


class BasketPageLocators:
    MESSAGE_EMPTY_LINK = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_PRODUCT_LINK = (By.CSS_SELECTOR, ".basket-items .price_color")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".add-to-basket .btn-add-to-basket")
    NAME_PRODUCT_LINK = (By.CSS_SELECTOR, ".product_page .product_main h1")
    STATUS_NAME_PRODUCT_LINK = (By.CSS_SELECTOR, ".alert:first-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success:first-child")
