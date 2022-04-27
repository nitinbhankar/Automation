from selenium.webdriver.common.by import By


class CustomerProfile:
    def __init__(self, driver):
        self.driver = driver

        self.enter_name_name = "name"
        self.enter_phone_name = "phone"
        self.enter_email_name = "email"
        self.enter_company_name = "company"
        self.enter_industry_name = "industry"
        self.enter_total_entities_name = "total_entities"
        self.enter_total_jurisdictions_name = "total_jurisdictions"
        self.enter_purpose_name = "purpose"
        self.enter_password_name = "password"
        self.enter_password_confirm_name = "password_confirm"
        self.next_button_xpath = "//*[@id='next-confirm-col']/button"

    def typename(self, name):
        self.driver.find_element(By.NAME, self.enter_name_name).clear()
        self.driver.find_element(By.NAME, self.enter_name_name).send_keys(name)

    def typephone(self, phone):
        self.driver.find_element(By.NAME, self.enter_phone_name).clear()
        self.driver.find_element(By.NAME, self.enter_phone_name).send_keys(phone)

    def typeemail(self, email):
        self.driver.find_element(By.NAME, self.enter_email_name).clear()
        self.driver.find_element(By.NAME, self.enter_email_name).send_keys(email)

    def typecompany(self, company):
        self.driver.find_element(By.NAME, self.enter_company_name).clear()
        self.driver.find_element(By.NAME, self.enter_company_name).send_keys(company)

    def typeindustry(self, industry):
        # self.driver.find_element(By.NAME, self.enter_industry_name).clear()
        self.driver.find_element(By.NAME, self.enter_industry_name).send_keys(industry)

    def typeentity(self, entity):
        self.driver.find_element(By.NAME, self.enter_total_entities_name).clear()
        self.driver.find_element(By.NAME, self.enter_total_entities_name).send_keys(entity)

    def typejuri(self, total_jurisdictions):
        self.driver.find_element(By.NAME, self.enter_total_jurisdictions_name).clear()
        self.driver.find_element(By.NAME, self.enter_total_jurisdictions_name).send_keys(total_jurisdictions)

    def typepurpose(self, purpose):
        # self.driver.find_element(By.NAME, self.enter_purpose_name).clear()
        self.driver.find_element(By.NAME, self.enter_purpose_name).send_keys(purpose)

    def typepassword(self, password):
        self.driver.find_element(By.NAME, self.enter_password_name).clear()
        self.driver.find_element(By.NAME, self.enter_password_name).send_keys(password)

    def typepasswordconfirm(self, password_confirm):
        self.driver.find_element(By.NAME, self.enter_password_confirm_name).clear()
        self.driver.find_element(By.NAME, self.enter_password_confirm_name).send_keys(password_confirm)

    def click_next(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()























        




