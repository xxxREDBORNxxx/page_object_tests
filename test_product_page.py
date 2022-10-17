from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.check_click_basket()  # проверяем кликабельность кнопки "Добавить в корзину"
    page.add_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # рассчитываем формулу из алерта и получаем ответ для курса
