import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language: es or fr")


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nЗапуск браузера для теста на {} языке..".format(user_language))
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nВыход из браузера..")
    browser.quit()