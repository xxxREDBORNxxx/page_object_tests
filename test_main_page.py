import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(5)
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логин
    time.sleep(5)
    page.should_be_login_link()
    time.sleep(5)
