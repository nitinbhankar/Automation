from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Formationfiling:

    def __init__(self, driver):
        self.driver = driver

        self.enter_entity_name_xpath = "//input[@placeholder ='Entity Name*']"
        self.enter_entity_state_xpath = "//select[@name='state[]']"
        self.enter_entity_type_xpath = "//select[@name='type[]']"
        self.click_next_xpath = "//*[@id='next-confirm-col']/button"

    def typeentityname(self, entityname):
        self.driver.find_element(By.XPATH, self.enter_entity_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_entity_name_xpath).send_keys(entityname)

    def typeentitystate(self, entitystate):
        self.driver.find_element(By.XPATH, self.enter_entity_state_xpath).send_keys(entitystate)

    def entitytype(self, entitytype):
        self.driver.find_element(By.XPATH, self.enter_entity_type_xpath).send_keys(entitytype)

    def clicknext(self):
        self.driver.find_element(By.XPATH, self.click_next_xpath).click()
