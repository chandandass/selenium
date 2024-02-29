import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:8281")

driver = webdriver.Chrome(options=options)

#provide website url here
driver.get("https://play.google.com/console/u/1/developers/6972297686594967503/app-list")

input = driver.find_element(By.CSS_SELECTOR, "input[name='filesToUpload']")
files_path = ['1.png','2.png','3.png']
current_dir = os.getcwd()
full_path = [os.path.join(current_dir,file_path) for file_path in files_path]
# input.clear()

# for i in full_path:

input.send_keys('\n'.join(full_path))
#   time.sleep(200)

time.sleep(5 * 1000)
driver.quit()