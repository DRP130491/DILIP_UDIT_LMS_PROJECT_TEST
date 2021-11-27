import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestStudentLoginLogout():

  def test_student1LoginLogout(self):
    self.driver = webdriver.Chrome()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Student").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("BDA04")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").send_keys("888")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs:nth-child(2)").click()
    sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(2)
    self.driver.quit()

  def test_student2LoginLogout(self):
    self.driver = webdriver.Chrome()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Student").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("BDA10")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").send_keys("999")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Heet Bodara").click()
    sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(2)
    self.driver.quit()