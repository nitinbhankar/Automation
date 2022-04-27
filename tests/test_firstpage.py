from selenium import webdriver
from pages.FirstPage import FirstPage
from pages.CustomerProfile import CustomerProfile
from pages.Createfiling import Createfiling
from pages.Formationfiling import Formationfiling
from pages.PlanDetails import PlanDetails
from pages.Billing import Billing
from pages.SignUp import SignUp
import pytest
import utils.utils as util


class Test_first_page:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()

    def test_first_page(self, test_setup):
        # URL
        driver.get(util.URL)
        # Landing page object
        firstpage = FirstPage(driver)
        firstpage.click_get_started()
        # Customer profile page object
        customerprofile = CustomerProfile(driver)
        customerprofile.typename(util.name)
        customerprofile.typephone(util.phone)
        customerprofile.typeemail(util.email)
        customerprofile.typecompany(util.company)
        customerprofile.typeindustry(util.industry)
        customerprofile.typeentity(util.entities)
        customerprofile.typepurpose(util.purpose)
        customerprofile.typepassword(util.password)
        customerprofile.typepasswordconfirm(util.cpassword)
        customerprofile.click_next()
        # Click filing page object
        clickfiling = Createfiling(driver)
        clickfiling.click_create_filing()
        # Formation Filing object
        formationfiling = Formationfiling(driver)
        formationfiling.typeentityname(util.entityname)
        formationfiling.typeentitystate(util.entitystate)
        formationfiling.entitytype(util.entitytype)
        formationfiling.clicknext()
        # Plan Details page Object
        plandetails = PlanDetails(driver)
        plandetails.click_next()
        # Billing Page Object
        billing = Billing(driver)
        billing.type_name_on_card(util.cardholder)
        billing.type_card_number(util.card)
        billing.type_date(util.expiry)
        billing.type_cvv(util.cvv)
        billing.type_billing(util.address)
        billing.type_city(util.city)
        billing.type_state(util.state)
        billing.type_zip(util.bzip)
        billing.click_confirm_purchase()
        driver.implicitly_wait(100)
        # final page Object
        signup = SignUp(driver)
        signup.click_on_continue()
























