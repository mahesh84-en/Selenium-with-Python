from selenium.webdriver.common.by import By



class ConfirmationPage:

    country = (By.ID, "country")
    country_name = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver

    def select_country(self):
        return self.driver.find_element(*ConfirmationPage.country)
    def select_country_name(self):
        return self.driver.find_element(*ConfirmationPage.country_name)
    def select_checkbox(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)
    def submit_button(self):
        return self.driver.find_element(*ConfirmationPage.submit)
    def alert_slected(self):
        return self.driver.find_element(*ConfirmationPage.alert)


