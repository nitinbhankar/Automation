from selenium.webdriver.common.by import By


class Billing:

    def __init__(self, driver):
        self.driver = driver

        self.name_on_card_xpath = "//input[@id = 'name-oncard']"
        self.card_number_xpath = "//input[@name = 'card[cardNumber]']"
        self.date_xpath = "//input[@placeholder = 'MM/YY']"
        self.cvv_xpath = "//input[@placeholder = 'CVV']"
        self.address_xpath = "//input[@placeholder = 'Billing Address']"
        self.city_xpath = "//input[@name = 'city']"
        self.state_xpath = "//select[@placeholder = 'State']"
        self.zip_xpath = "//input[@placeholder = 'Zip']"
        self.confirm_purchase = "//*[@id='next-confirm-col']/button"

    def type_name_on_card(self, cardholder):
        self.driver.find_element(By.XPATH, self.name_on_card_xpath).send_keys(cardholder)

    def type_card_number(self, card):
        self.driver.find_element(By.XPATH, self.card_number_xpath).send_keys(card)

    def type_date(self, date):
        self.driver.find_element(By.XPATH, self.date_xpath).send_keys(date)

    def type_cvv(self, expiry):
        self.driver.find_element(By.XPATH, self.cvv_xpath).send_keys(expiry)

    def type_billing(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).clear()
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def type_city(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

    def type_state(self, state):
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)

    def type_zip(self, bzip):
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys(bzip)

    def click_confirm_purchase(self):
        self.driver.find_element(By.XPATH, self.confirm_purchase).click()
