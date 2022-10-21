import time

import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('param',
                         [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_" \
           f"207/?promo=offer{param}"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.check_click_basket()  # проверяем кликабельность кнопки "Добавить в корзину"
    page.add_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # рассчитываем формулу из алерта и получаем ответ для курса
    page.compare_product_names()  # сравниваем название товара в корзине и в сообщении статуса


@pytest.mark.login_link
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_link
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логин
    page.should_be_login_link()  # проверяем ссылку на страницу логина


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


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.should_be_basket_link()
    page.go_to_basket_page()
    time.sleep(10)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()  # TODO: only for the default language=ru
    basket_page.should_not_be_product()
    basket_page.should_be_message_empty()
