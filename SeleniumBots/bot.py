from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from sys import argv
from random import randint

#DOMAIN = "https://gttx.app/"
DOMAIN = "http://localhost:5173/"
FINALQ = "The bot will self destruct after this question."
TIME = 10

def response():
    return responses[randint(0,(len(responses) - 1))]

options = webdriver.FirefoxOptions()

#Solo
browser = webdriver.Firefox(options=options)
#Grid
#browser = webdriver.Remote('192.168.56.1',options=options)

responses = open("responses.txt", 'r').readlines()


browser.get(DOMAIN+'login')
WebDriverWait(browser, TIME).until(EC.staleness_of(browser.find_element(By.ID, 'email')))

elem = browser.find_element(By.ID, 'email')
elem.send_keys(argv[1] + Keys.TAB + argv[2])

WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'login_button')))
elem.send_keys(Keys.RETURN)
WebDriverWait(browser, TIME).until(EC.url_matches(DOMAIN+'dashboard'))


try:
    browser.get(DOMAIN+'dashboard/notes?roomid='+argv[3])
except:
    print("invalid Room")

WebDriverWait(browser, TIME).until(EC.presence_of_element_located((By.ID, 'curr_question')))


last_question = ""
try:
    while(last_question != FINALQ):
        question = browser.find_element(By.ID, 'curr_question').text
        if (question != last_question):
            last_question = question
            answer = browser.find_element(By.ID, 'notes')
            answer.click()
            answer.clear()
            answer.send_keys(response())
            browser.find_element(By.ID, 'submit_answer').click()

        else:
            sleep(1)
except KeyboardInterrupt:
    print("Stopped.")
    browser.quit()
    exit()
browser.quit()