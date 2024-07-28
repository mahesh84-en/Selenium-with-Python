from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    products = (By.XPATH,"//div[@class='card h-100']" )
    add_to_cart = (By.XPATH, "div/button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def get_all_products(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def click_on_add_to_cart(self):
        return self.driver.find_element(*CheckoutPage.add_to_cart)

    def click_on_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirmationpage = ConfirmationPage(self.driver)
        return confirmationpage