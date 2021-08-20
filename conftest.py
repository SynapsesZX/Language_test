from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import pytest



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages': user_language})
        driver = webdriver.Chrome(executable_path='C:\Selenium Chrome\chromedriver.exe')
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox('D:\Automation\Gecko Driver\geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()




