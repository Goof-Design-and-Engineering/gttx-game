from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from sys import argv
from random import randint


options = webdriver.FirefoxOptions()
options.add_argument("--headless")

#Solo
#browser = webdriver.Firefox(options=options)
#Grid
browser = webdriver.Remote('192.168.0.123:4444',options=options)

browser.get("https://www.gttx.app")
print("start")
sleep(120)
print("finished")
browser.quit()