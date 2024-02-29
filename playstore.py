import time
from selenium.webdriver.common.by import By
class Playstore:
  def __init__(self,driver,url) -> None:
    self.driver = driver
    self.driver.get("https://play.google.com/console/u/0/developers/6972297686594967503/app/4976256644804544907/app-dashboard?timespan=thirtyDays")
    time.sleep(4)
    element = self.driver.find_element(By.CSS_SELECTOR, 'a.row-anchor[href$="app-content/overview"]')
    time.sleep(2)
    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(3)

  def back_app_content(self):
    time.sleep(2)
    appcontent_back_button = self.driver.find_element(By.XPATH, "//a[@aria-label='Go back to App content']")
    appcontent_back_button.click()

  def privacy_policy(self, deleteURl):
    try:
      time.sleep(3)
      input = self.driver.find_element(By.XPATH, "//input[@aria-label='Privacy policy URL']")
      time.sleep(2)
      input.send_keys(deleteURl)
      time.sleep(1)
      save_button = self.driver.find_element(By.XPATH, "//button[@debug-id='main-button']")
      save_button.click()
      return True
    except Exception as e:
      return None

  def ads_app(self):
    pass
  def app_access(self):
    pass
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