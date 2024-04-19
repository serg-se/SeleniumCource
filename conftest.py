import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose interface language")


@pytest.fixture(scope="session")
def user_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="session")
def options(request, user_language):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    return options


@pytest.fixture(scope="function")
def browser(options):
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
