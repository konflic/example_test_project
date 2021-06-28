import pytest
from selenium import webdriver

@pytest.fixture
def browser(request):
    """Basic browser fixture for testing"""
    browser = webdriver.Chrome()
    request.addfinalizer(browser.close)
    return browser




