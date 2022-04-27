from selenium.webdriver.common.by import By


class PlanDetails:

    def __init__(self, driver):
        self.driver = driver

        self.click_next_xpath = "//*[@id='next-confirm-col']/button"

    def click_next(self):
        self.driver.find_element(By.XPATH, self.click_next_xpath).click()
