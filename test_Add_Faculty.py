import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAddFaculty():

  def test_addFaculty(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("AD001")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    self.driver.find_element(By.NAME, "userpassword").send_keys("111")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Tables").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Faculty Details").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
    sleep(1)
    self.driver.find_element(By.ID, "example-input-medium").click()
    self.driver.find_element(By.ID, "example-input-medium").send_keys("Pragnesh")
    sleep(1)
    #self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(2)").click()
    self.driver.find_element(By.NAME, "fac_lname").click()
    self.driver.find_element(By.NAME, "fac_lname").send_keys("Trivedi")
    sleep(1)
    self.driver.find_element(By.ID, "example-input-small").click()
    self.driver.find_element(By.ID, "example-input-small").send_keys("9999999999")
    sleep(1)
    self.driver.find_element(By.NAME, "fac_mail").click()
    self.driver.find_element(By.NAME, "fac_mail").send_keys("example@yahoo.com")
    sleep(1)
    self.driver.find_element(By.NAME, "fac_number").click()
    self.driver.find_element(By.NAME, "fac_number").send_keys("8833442211")
    sleep(1)
    self.driver.find_element(By.NAME, "fac_pass").click()
    self.driver.find_element(By.NAME, "fac_pass").send_keys("faculty@123")
    sleep(1)
    self.driver.find_element(By.NAME, "fac_repass").send_keys("faculty@123")
    self.driver.find_element(By.NAME, "btn_sub").click()
    sleep(2)
    self.driver.find_element(By.NAME, "fac_photo_u").send_keys("//home//vvdn//Downloads//aaaaa.jpeg")
    sleep(1)
    self.driver.find_element(By.NAME, "btn_sub").click()
    sleep(1)
    self.driver.quit()

  
