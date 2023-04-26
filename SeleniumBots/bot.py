from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()

browser = webdriver.Firefox(options=options)


browser.get('https://gttx.app/login')
elem = browser.find_element(By.NAME, 'email')
elem.send_keys('bot0@gttx.app' + Keys.TAB + 'bot0pass')
sleep(0.5)
elem.send_keys(Keys.RETURN)
sleep(2)
browser.get('https://gttx.app/dashboard/notes?gqkvmzpivxxxz6o')
sleep(1)

last_question = ""
try:
    while(True):
        question = browser.find_element(By.ID, 'curr_question').text
        if (question != last_question):
            last_question = question
            answer = browser.find_element(By.ID, 'notes')
            answer.send_keys('This is a test.')
            browser.find_element(By.ID, 'submit_answer').click()

        else:
            browser.refresh()
            sleep(10)
except KeyboardInterrupt:
    pass
browser.quit()