import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAddAdmin():

  def test_addAdmin(self):
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
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Tables").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Admin Details").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
    sleep(1)
    self.driver.find_element(By.ID, "example-input-medium").click()
    self.driver.find_element(By.ID, "example-input-medium").send_keys("Dilip")
    sleep(1)
    self.driver.find_element(By.NAME, "admin_lname").click()
    self.driver.find_element(By.NAME, "admin_lname").send_keys("Patel")
    sleep(1)
    self.driver.find_element(By.ID, "example-input-small").click()
    self.driver.find_element(By.ID, "example-input-small").send_keys("0986712345")
    sleep(1)
    self.driver.find_element(By.NAME, "admin_mail").click()
    self.driver.find_element(By.NAME, "admin_mail").send_keys("example@gmail.com")
    sleep(1)
    self.driver.find_element(By.NAME, "admin_number").click()
    self.driver.find_element(By.NAME, "admin_number").send_keys("9157820758")
    sleep(1)
    self.driver.find_element(By.NAME, "admin_pass").click()
    self.driver.find_element(By.NAME, "admin_pass").send_keys("admin@123")
    sleep(1)
    self.driver.find_element(By.NAME, "admin_repass").send_keys("admin@123")
    self.driver.find_element(By.NAME, "btn_sub").click()
    sleep(2)
    self.driver.find_element(By.NAME, "admin_photo_u").send_keys("//home//vvdn//Downloads//aaaaa.jpeg")
    sleep(1)
    self.driver.find_element(By.NAME, "btn_sub").click()
    sleep(1)
    self.driver.quit()

  
