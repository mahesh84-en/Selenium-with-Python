from selenium.webdriver.common.by import By

from pageObjects.checkoutpage import CheckoutPage


class Homepage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "a[href*='name']")
    email = (By.XPATH, "a[href*='email']")
    check = (By.XPATH, "a[href*='check']")
    drop_down = (By.XPATH, "a[href*='dropdown']")
    submit = (By.XPATH, "//a[@class= 'submit']")
    alert = (By.XPATH, "//a[@class= 'alert_text']")

    def __init__(self, driver):
        self.browser = driver

    def shopItems(self):
        self.browser.find_element(*Homepage.shop).click()
        checkoutpage = CheckoutPage(self.browser)
        return checkoutpage


    def get_Name(self):
        return self.browser.find_element(*Homepage.name)

    def get_email(self):
        return self.browser.find_element(*Homepage.email)

    def get_check(self):
        return self.browser.find_element(*Homepage.check)

    def get_dropdown(self):
        return self.browser.find_element(*Homepage.drop_down)

    def get_submit(self):
        return self.browser.find_element(*Homepage.submit)

    def get_alert(self):
        return self.browser.find_element(*Homepage.alert)