import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
try:


    # Provide website URL here
    driver.get("https://play.google.com/console/u/0/developers/6972297686594967503/app/4976256644804544907/app-dashboard?timespan=thirtyDays")
    time.sleep(3)
    # element = driver.find_element(By.XPATH, '//*[@id="console-root-021280"]/console-chrome/div/header/div/div/a/img')
    element = driver.find_element(By.CSS_SELECTOR, 'a.row-anchor[href$="app-content/overview"]')
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "//button[@aria-label = 'Start Privacy policy declaration']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(2)
    button.click()
    time.sleep(5)
    input = driver.find_element(By.XPATH, "//input[@aria-label='Privacy policy URL']")
    time.sleep(3)
    input.send_keys("https://bluebirdlanguages.com/bluebird-languages-privacy-policy/")
    # exit()


    # Sleep for 5 seconds
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()