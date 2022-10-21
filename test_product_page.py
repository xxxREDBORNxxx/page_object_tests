import time
import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.registration
class TestUserAddToBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_active_register_input_form()
        page.register_new_user()
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)

        page.open()
        page.check_click_basket()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()  # TODO: only for stepic lessons
        page.compare_product_names()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)

        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('param',
                         [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_" \
           f"207/?promo=offer{param}"
    page = ProductPage(browser, link)

    page.open()
    page.check_click_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # TODO: only for stepic lessons
    page.compare_product_names()


@pytest.mark.login_link
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)

    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.login_link
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)

    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.message
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)

    page.open()
    page.check_click_basket()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.message
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)

    page.open()
    page.should_not_be_success_message()


@pytest.mark.message
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)

    page.open()
    page.check_click_basket()
    page.add_to_basket()
    page.success_message_should_disappear()


@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)

    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()

    time.sleep(5)  # TODO: only for debug

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()  # TODO: only for the default language=ru
    basket_page.should_not_be_product()
    basket_page.should_be_message_empty()
