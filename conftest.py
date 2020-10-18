import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    """Basic browser fixture for testing"""
    driver = webdriver.Chrome()
    request.addfinalizer(driver.close)
    return driver
