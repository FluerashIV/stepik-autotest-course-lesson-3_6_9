import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    print("\nStart Chrome browser for test with", user_language, "language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    # else:
    #     raise pytest.UsageError("--language should be correct")
    yield browser
    print("\nQuit browser")
    browser.quit()
