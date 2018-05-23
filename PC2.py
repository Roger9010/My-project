# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class FIrst(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_f_irst(self):
        driver = self.driver
        driver.get('http://www.sat.gob.mx/Paginas/Inicio.aspx')
        driver.find_element_by_xpath('//a[contains(@href,¨javascript:;¨)]').click()
        driver.find_element_by_link_text(u'Trámites').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath('//map[@id=¨Map¨]/area[2]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id('rfc').click()
        driver.find_element_by_id('rfc').clear()
        driver.find_element_by_id('rfc').send_keys('gamr901020gk9')
        driver.find_element_by_id('Ecom_Password').clear()
        driver.find_element_by_id('Ecom_Password').send_keys('8seconds')
        driver.find_element_by_id('iniciaSesion').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        self.assertEqual(u'Aviso importante:\n \nLos Recursos de Revocación deberán presentarse por Buzón Tributario.', self.close_alert_and_get_its_text())
    
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
