from selenium.webdriver.common.by import By


class Createfiling:

    def __init__(self, driver):
        self.driver = driver

        self.click_create_filing_button_xpath = "/html/body/div[2]/div/div[2]/a[1]"

    def click_create_filing(self):
        self.driver.find_element(By.XPATH, self.click_create_filing_button_xpath).click()



