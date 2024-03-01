from playstore import Playstore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)

playstore = Playstore(driver,"https://play.google.com/console/u/0/developers/6972297686594967503/app/4972916644633533485/app-content/overview")


# playstore.privacy_policy("hello world")
playstore.app_access()