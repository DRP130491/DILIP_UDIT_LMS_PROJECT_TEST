import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestFacultyLoginLogout():

  def test_faculty1LoginLogout(self):
    self.driver = webdriver.Chrome()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Faculty").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("LEC01")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").send_keys("123")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .hidden-xs").click()
    sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(1)
    self.driver.quit()

  def test_faculty2LoginLogout(self):
    self.driver = webdriver.Chrome()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    self.driver.find_element(By.LINK_TEXT, "Faculty").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("LEC02")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").send_keys("345")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .hidden-xs").click()
    sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(1)
    self.driver.quit()
