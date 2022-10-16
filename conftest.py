import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_firefox


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose correct language for site, default='ru'")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":

        print("\nstart chrome browser for test..")

        options = Options_chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # избавляемся от сообщения журнала: 'DevTools listening on ws://....'
        # Suppressing any console message either from the Selenium driver or from the browser itself,
        # including the first DevTools message listening to ws://127.0.0.1 at the very beginning.
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":

        print("\nstart firefox browser for test..")

        options = Options_firefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
