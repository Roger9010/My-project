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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.google.com.mx/search?q=occ&rlz=1C1CHZL_esMX748MX749&oq=occ&aqs=chrome..69i57j69i60l2j0l3.1350j0j8&sourceid=chrome&ie=UTF-8")
        driver.find_element_by_link_text(u"Bolsa de Trabajo, Ofertas de empleo, trabajos | OCCMundial México").click()
        driver.find_element_by_link_text("Crear cuenta gratis").click()
        driver.find_element_by_id("new-account-name").click()
        driver.find_element_by_id("new-account-name").clear()
        driver.find_element_by_id("new-account-name").send_keys("ROGELIO GARCIA MARTINEZ")
        driver.find_element_by_id("new-account-email").clear()
        driver.find_element_by_id("new-account-email").send_keys("rogelio.garcia@enroutesystems.com")
        driver.find_element_by_id("new-account-password").click()
    
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
