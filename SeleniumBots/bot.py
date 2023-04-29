from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from sys import argv
from random import randint

DOMAIN = "https://gttx.app/"
#DOMAIN = "http://localhost:5173/"
FINALQ = "The bot will self destruct after this question."
TIME = 60

BOT_NUM = argv[4]


def report_time(time, value):
    print(value + "\t" + str(BOT_NUM) + "\t" + str(time))

def response():
    return responses[randint(0,(len(responses) - 1))]

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
#Solo
browser = webdriver.Firefox(options=options)
#Grid
#browser = webdriver.Remote('192.168.56.1',options=options)

responses = open("responses.txt", 'r').readlines()

start_time = time.time()
browser.get(DOMAIN+'login')
report_time(time.time() - start_time, "login")
WebDriverWait(browser, TIME).until(EC.staleness_of(browser.find_element(By.ID, 'email')))

elem = browser.find_element(By.ID, 'email')
elem.send_keys(argv[1] + Keys.TAB + argv[2])
WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'login_button')))
elem.send_keys(Keys.RETURN)
WebDriverWait(browser, TIME).until(EC.url_contains('dashboard'))

load_time = time.time()
browser.get(DOMAIN+'dashboard')
report_time(time.time() - load_time, "dashb")

load_time = time.time()
browser.get(DOMAIN+'start')
report_time(time.time() - load_time, "start")

WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'invite')))
elem = browser.find_element(By.ID, 'invite')
elem.send_keys(argv[3])
WebDriverWait(browser, TIME).until(EC.element_to_be_clickable(browser.find_element(By.ID, 'invite_button')))
elem.send_keys(Keys.RETURN)

###FOR TEST
browser.quit()
exit()
###TSET ROF
WebDriverWait(browser, TIME).until(EC.presence_of_element_located((By.ID, 'curr_question')))
report_time(time.time() - start_time, "ttbr")

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