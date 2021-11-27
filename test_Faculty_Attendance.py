import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestFacultyAttendance():

  def test_facultyAttendance(self):
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
    self.driver.find_element(By.LINK_TEXT, "Faculty Attendance").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".in:nth-child(2) a").click()
    sleep(1)
    #self.driver.find_element(By.NAME, "DOA").click()
    sleep(1)
    self.driver.find_element(By.NAME, "DOA").send_keys("27-11-2021")
    sleep(2)
    self.driver.find_element(By.ID, "radio3").click()
    sleep(2)
    self.driver.find_element(By.NAME, "PorA2").click()
    sleep(2)
    self.driver.find_element(By.NAME, "btn_sub").click()
    sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs:nth-child(2)").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    sleep(1)
    self.driver.quit()
  
