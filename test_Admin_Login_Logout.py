import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAdminLoginLogout():
  def test_adminLoginLogout(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("AD001")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").send_keys("111")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "HH BODARA").click()
    sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(1)
    self.driver.quit()
