import pytest
from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.Homepage import Homepage
from pageObjects.checkoutpage import CheckoutPage
from utilities.test_base_class import TestBase


@pytest.mark.usefixtures("browser")
#using the inheritance concept
class TestOne(TestBase):


    def test_end_to_end(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        checkout = homepage.shopItems()
        log.info("navigating to the products")
        products = checkout.get_all_products()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkout.click_on_add_to_cart()
        log.info("navigated to the product page")
        confirmationpage = checkout.click_on_checkout_button()
        confirmationpage.select_country().click()
        confirmationpage.select_country_name().send_keys("ind")
        self.verify_link_presence("India")

        confirmationpage.select_country_name().click()
        confirmationpage.select_checkbox().click()
        confirmationpage.submit_button()
        successText = confirmationpage.alert_slected().text
        assert "Success! Thank you!" in successText
