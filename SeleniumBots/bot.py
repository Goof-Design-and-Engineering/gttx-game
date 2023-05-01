from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv
from random import randint

DOMAIN = "https://gttx.app/"
#DOMAIN = "http://localhost:5173/"
FINALQ = "Final Question. Bots should terminate after they answer it."
TIME = 60

BOT_NUM = argv[4]



def response():
    return responses[randint(0,(len(responses) - 1))]

options = webdriver.FirefoxOptions()
#options.add_argument("--headless")
#Solo
#browser = webdriver.Firefox(options=options)
#Grid
browser = webdriver.Remote('192.168.0.123:4444',options=options)

responses = open("responses.txt", 'r').readlines()

browser.get(DOMAIN+'login')
WebDriverWait(browser, TIME).until(EC.staleness_of(browser.find_element(By.ID, 'email')))

elem = browser.find_element(By.ID, 'email')
elem.send_keys(argv[1] + Keys.TAB + argv[2])
WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'login_button')))
elem.send_keys(Keys.RETURN)
WebDriverWait(browser, TIME).until(EC.url_contains('dashboard'))
browser.get(DOMAIN+'start')
WebDriverWait(browser, TIME).until(EC.presence_of_element_located((By.ID, argv[3])))
WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, argv[3])))
browser.find_element(By.ID, argv[3]).click()


WebDriverWait(browser, TIME).until(EC.presence_of_element_located((By.ID, 'curr_question')))
print(browser.find_element(By.ID, 'curr_question').text)
WebDriverWait(browser, TIME).until_not(EC.text_to_be_present_in_element((By.ID, 'curr_question'), "Loading current question..."))


last_question = None
try:
    while(last_question != FINALQ):
        question = browser.find_element(By.ID, 'curr_question')
        q_text = question.text
        if (q_text != last_question):
            last_question = q_text
            answer = browser.find_element(By.ID, 'notes')
            answer.click()
            answer.clear()
            answer.send_keys(response())
            WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'submit_answer')))
            browser.find_element(By.ID, 'submit_answer').click()

        else:
            WebDriverWait(browser, timeout=3600).until_not(EC.text_to_be_present_in_element((By.ID, 'curr_question'), q_text))
except KeyboardInterrupt:
    print("Stopped.")
    browser.quit()
    exit()
browser.quit()