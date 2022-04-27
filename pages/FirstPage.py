from selenium.webdriver.common.by import By


class FirstPage:

    def __init__(self, driver):
        self.driver = driver

        self.get_started_button_xpath = "//*[@id='setup-account']/button"

    def click_get_started(self):
        self.driver.find_element(By.XPATH, self.get_started_button_xpath).click()






