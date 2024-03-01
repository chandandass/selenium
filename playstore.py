

import time
from selenium.webdriver.common.by import By
class Playstore:
  def __init__(self,driver,url) -> None:
    self.driver = driver
    self.driver.get(url)
    time.sleep(4)
    element = self.driver.find_element(By.CSS_SELECTOR, 'a.row-anchor[href$="app-content/overview"]')
    time.sleep(2)
    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(2)

  def back_app_content(self):
    time.sleep(2)
    appcontent_back_button = self.driver.find_element(By.XPATH, "//a[@aria-label='Go back to App content']")
    appcontent_back_button.click()

  def privacy_policy(self, deleteURl):
    try:
      button = self.driver.find_element(By.XPATH, "//button[@aria-label = 'Start Privacy policy declaration']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", button)
      time.sleep(2)
      button.click()
      time.sleep(3)
      input = self.driver.find_element(By.XPATH, "//input[@aria-label='Privacy policy URL']")
      time.sleep(2)
      input.send_keys(deleteURl)
      time.sleep(1)
      self.back_app_content()
      # save_button = self.driver.find_element(By.XPATH, "//button[@debug-id='main-button']")
      # save_button.click()
      return True
    except Exception as e:
      return None

  def ads_app(self):
    button = self.driver.find_element(By.XPATH, "//button[@aria-label = 'Start Ads declaration']")
    button.click()
    time.sleep(2)
    no_button = self.driver.find_element(By.XPATH, "//label[text() = 'No, my app does not contain ads']")
    time.sleep(1)
    no_button.click()
    time.sleep(2)
    save = self.driver.find_element(By.XPATH, "//span[text() = 'Save']")
    print(save)
    #  driver.execute_script("arguments[0].scrollIntoView(true);", element)
    pass
  def app_access(self, first, second, third, fourth):
    button = self.driver.find_element(By.XPATH, "//button[@aria-label = 'Start App access declaration']")
    time.sleep(2)
    button.click()
    time.sleep(2)
    no_button = self.driver.find_element(By.XPATH, "//label[text() = 'All or some functionality in my app is restricted']")
    self.driver.execute_script("arguments[0].scrollIntoView(true);", no_button)
    time.sleep(1)
    no_button.click()
    time.sleep(1)
    add_instructions = self.driver.find_element(By.XPATH, "//span[text() = 'Add instructions']")
    time.sleep(2)
    add_instructions.click()
    time.sleep(1)
    input1 = self.driver.find_element(By.XPATH, "(//input)[5]")
    input1.send_keys(first)

    input1 = self.driver.find_element(By.XPATH, "(//input)[6]")
    input1.send_keys(second)

    input1 = self.driver.find_element(By.XPATH, "(//input)[7]")
    time.sleep(1)
    input1.send_keys(third)

    input1 = self.driver.find_element(By.XPATH, "(//textarea)")
    time.sleep(1)
    input1.send_keys(fourth)

    input1 = self.driver.find_element(By.XPATH, "(//input)[8]")
    input1.click()
    add = self.driver.find_element(By.XPATH, "//span[text() = 'Add']")
    print(add)
  def content_rating(self):
    pass
  def target_audience(self):
    pass
  def news_apps(self):
    pass
  def covid19_apps(self):
    pass
  def data_safety(self):
    pass
  def advertising(self):
    pass
  def goverment_app(self):
    pass
  def finalcial_feature(self):
    pass