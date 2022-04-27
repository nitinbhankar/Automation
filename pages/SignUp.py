from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self, driver):
        self.driver = driver

        self.click_on_continue_xpath = "/html/body/div[1]/div/button"

    def click_on_continue(self):
        self.driver.find_element(By.XPATH, self.click_on_continue_xpath)

