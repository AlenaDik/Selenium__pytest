import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome() #executable_path="./chromedriver")
    yield driver
    driver.quit()