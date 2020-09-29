import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    """Basic browser fixture for testing"""
    driver = webdriver.Chrome()

    def fin():
        driver.close()

    request.addfinalizer(fin)

    return driver
