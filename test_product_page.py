import pytest

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


