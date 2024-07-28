import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
import inspect
import logging

@pytest.mark.usefixtures("browser")
class TestBase:

    #injecting the logging to framerork
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.WARNING)
        return logger

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, text)))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    #created the data to pass to the test using get_data fixture
    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_Data(self, request):
        return request.params


