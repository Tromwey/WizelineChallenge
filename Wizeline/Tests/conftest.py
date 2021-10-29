import pytest
import sys

sys.path.append("../")

from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["edge", "chrome"], scope='class')
def init_driver(request):
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path=TestData.EDGE_DRIVER_PATH)
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()