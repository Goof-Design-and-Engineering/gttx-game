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
FINALQ = "Final Question. Bots should terminate after they answer it."
TIME = 30



def time_page(page, name=None):
    start_time = time.time()
    browser.get(DOMAIN+page)
    ttl = time.time() - start_time
    if name == None:
        print(page + "\t" + str(ttl))
    else:
        print(name + "\t" + str(ttl))



options = webdriver.FirefoxOptions()
options.add_argument("--headless")
#Solo
browser = webdriver.Firefox(options=options)
#Grid
#browser = webdriver.Remote('192.168.0.123:4444',options=options)

responses = open("responses.txt", 'r').readlines()
time_page('', "index")
time_page('login')
#WebDriverWait(browser, TIME).until(EC.staleness_of(browser.find_element(By.ID, 'email')))

elem = browser.find_element(By.ID, 'email')
elem.send_keys(argv[1] + Keys.TAB + argv[2])
WebDriverWait(browser, TIME).until(EC.element_to_be_clickable((By.ID, 'login_button')))
elem.send_keys(Keys.RETURN)
WebDriverWait(browser, TIME).until(EC.url_contains('dashboard'))
time_page('dashboard', 'dashb')
time_page('start')
time_page('dashboard/notes', 'notes')



browser.quit()