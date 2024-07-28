from selenium.webdriver.support.select import Select

from pageObjects.Homepage import Homepage
from utilities.test_base_class import TestBase


class TestHomePage(TestBase):

    def test_form_submission(self, get_Data):

        homepage = Homepage(self.driver)
        homepage.get_Name().send_keys(get_Data["first_name"])
        homepage.get_email().send_keys(get_Data["last_name"])
        homepage.get_check().click()
        self.select_option_by_text(homepage.drop_down, get_Data["gender"])
        homepage.get_submit().click()
        alert_text = homepage.get_alert().text
        assert ("success" in alert_text)
        self.driver.refresh()


