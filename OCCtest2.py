# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Third(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_third(self):
        driver = self.driver
        driver.get("https://www.occ.com.mx/cuenta/nueva")
        driver.find_element_by_id("new-account-name").clear()
        driver.find_element_by_id("new-account-name").send_keys("ROGELIO GARCIA MARTINEZ")
        driver.find_element_by_id("new-account-email").clear()
        driver.find_element_by_id("new-account-email").send_keys("rogelio.garcia@enroutesystems.com")
        driver.find_element_by_id("new-account-password").clear()
        for _ in xrange(5):
            password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(13))
            driver.find_element_by_id("new-account-password").send_keys(password)
            assert driver.find_element_class_name('password-conditions')
            assert driver.find_element_class_name('length accomplished')
            assert driver.find_element_class_name('one-numer accomplished')
            assert driver.find_element_class_name('one-leeter accomplished')

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
