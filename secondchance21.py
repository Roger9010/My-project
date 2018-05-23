# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://espanol.yahoo.com/")
        driver.find_element_by_id("uh-signin").click()
        driver.find_element_by_id("createacc").click()
        driver.find_element_by_id("usernamereg-firstName").click()
        driver.find_element_by_id("usernamereg-firstName").clear()
        driver.find_element_by_id("usernamereg-firstName").send_keys("Rogelio")
        driver.find_element_by_id("usernamereg-lastName").clear()
        driver.find_element_by_id("usernamereg-lastName").send_keys("Garcia")
        driver.find_element_by_id("usernamereg-yid").click()
        driver.find_element_by_id("usernamereg-yid").clear()
        driver.find_element_by_id("usernamereg-yid").send_keys("garciarogelio405")
        driver.find_element_by_xpath("//div[@id='yid-field-suggestion']/div/p").click()
        driver.find_element_by_id("usernamereg-password").click()
        driver.find_element_by_id("usernamereg-phone").click()
        driver.find_element_by_id("usernamereg-phone").clear()
        driver.find_element_by_id("usernamereg-phone").send_keys("8110162876")
        driver.find_element_by_id("usernamereg-month").click()
        Select(driver.find_element_by_id("usernamereg-month")).select_by_visible_text("Octubre")
        driver.find_element_by_id("usernamereg-month").click()
        driver.find_element_by_name("shortCountryCode").click()
        driver.find_element_by_name("shortCountryCode").click()
        driver.find_element_by_id("usernamereg-day").click()
        driver.find_element_by_id("usernamereg-day").clear()
        driver.find_element_by_id("usernamereg-day").send_keys("20")
        driver.find_element_by_id("usernamereg-year").click()
        driver.find_element_by_id("usernamereg-year").clear()
        driver.find_element_by_id("usernamereg-year").send_keys("1990")
        driver.find_element_by_id("usernamereg-freeformGender").click()
        driver.find_element_by_id("regform").click()
        driver.find_element_by_id("usernamereg-phone").click()
        driver.find_element_by_id("usernamereg-password").click()
        driver.find_element_by_id("usernamereg-password").clear()
        driver.find_element_by_id("usernamereg-password").send_keys("8seconds")

    def passw_check() :
    passin = raw_input('Enter the password')

    if len(passin) == 8:
        if sum(map(str.isupper, passin)) == 2:
            if sum(map(str.islower, passin)) == 2:
                if sum (map(str.isdigit, passin)) == 4:
                    print('Password Okay')
                else: 
                    print('Not Okay!')

passw_check()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
