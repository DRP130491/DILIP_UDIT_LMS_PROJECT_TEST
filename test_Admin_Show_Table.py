import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAdminShowTable():

  def test_adminShowTable(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
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
    self.driver.find_element(By.LINK_TEXT, "Admin Details").click()
    sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Faculty Details").click()
    sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Student Details").click()
    sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(1)
    self.driver.quit()