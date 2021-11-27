import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestAnnouncementFaculty():

  def test_announcementFaculty(self):
    self.driver = webdriver.Chrome()
    sleep(1)
    self.driver.get("http://localhost/guni/main/")
    self.driver.maximize_window()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()

    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("AD001")
    sleep(1)
    self.driver.find_element(By.NAME, "userpassword").click()
    self.driver.find_element(By.NAME, "userpassword").send_keys("111")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Announcement").click()
    sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Announcement Form").click()
    sleep(1)
    self.driver.find_element(By.NAME, "annou_title").click()
    self.driver.find_element(By.NAME, "annou_title").send_keys("Exam Time Table")
    sleep(1)
    self.driver.find_element(By.NAME, "annou_content").click()
    self.driver.find_element(By.NAME, "annou_content").click()
    self.driver.find_element(By.NAME, "annou_content").send_keys("Announcement to all faculty to check exam time table")
    sleep(1)
    self.driver.find_element(By.CLASS_NAME, "col-sm-12").click()
    sleep(2)
    self.driver.find_element(By.NAME, "annou_file").send_keys("//home//vvdn//Downloads//tt.pdf")
    sleep(1)
    self.driver.find_element(By.NAME, "btn_sub_fac").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Show Faculty Announcements").click()
    sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Exam Time Table").click()
    sleep(3)
    self.driver.find_element(By.CLASS_NAME, "close").click()
    sleep(1)
    self.driver.quit()
  
