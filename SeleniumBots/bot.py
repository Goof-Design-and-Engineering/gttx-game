from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()

browser = webdriver.Remote('192.168.56.1:4444', options=options)


browser.get('https://gttx.app/login')
elem = browser.find_element(By.NAME, 'email')
elem.send_keys('bot0@gttx.app' + Keys.TAB + 'bot0pass')
sleep(0.5)
elem.send_keys(Keys.RETURN)
sleep(2)
browser.get('https://gttx.app/dashboard/notes?gqkvmzpivxxxz6o')
sleep(1)
#facilitator toggle
browser.find_element(By.CLASS_NAME, 'svelte-ao2ii4').click()


last_question = ""
try:
    while(True):
        sleep(1)
except KeyboardInterrupt:
    browser.quit()