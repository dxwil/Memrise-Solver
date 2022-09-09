#REQUIRMENTS:
#Python
#Selenium: pip3 install selenium
#Chrome
#chromedriver: https://chromedriver.chromium.org/
#Set words per session to 15

google_email = ''
google_pass = ''
PATH = ''
courseid = 





#Script start

toreview = int(input('How many words do you want to review? (Max 1000 per time): '))

import json
from unittest import skip
from wsgiref.validate import IteratorWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
driver = webdriver.Chrome(PATH)

driver.get(f'https://app.memrise.com/aprender/speed?course_id={courseid}')
sleep(2)


if 0 < toreview <= 100:
    todo = 1
elif 100 < toreview <= 200:
    todo = 2
elif 200 < toreview <= 300:
    todo = 3
elif 300 < toreview <= 400:
    todo = 4
elif 400 < toreview <= 500:
    todo = 5
elif 500 < toreview <= 600:
    todo = 6
elif 600 < toreview <= 700:
    todo = 7
elif 700 < toreview <= 800:
    todo = 8
elif 800 < toreview <= 900:
    todo = 9
elif 900 < toreview <= 1000:
    todo = 10


#Log in with google popup
main_page = driver.current_window_handle
driver.find_element(By.ID, 'google-btn').click()
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)
driver.find_element(By.ID, 'identifierId').send_keys(google_email)
driver.find_element(By.ID, 'identifierNext').click()
sleep(2)
actions = ActionChains(driver)
actions.send_keys(google_pass)
actions.perform()
driver.find_element(By.ID, 'passwordNext').click()
driver.switch_to.window(main_page)
sleep(10)


f = open('memrise.json')
data = json.load(f)

words1 = [p["words"] for p in data["levels"].values()]
definitions1 = [p["definitions"] for p in data["levels"].values()]

words = [item for sublist in words1 for item in sublist]
definitions = [item for sublist in definitions1 for item in sublist]

done = 0

while True:
    try:
            question = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/h2')
            opt1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/button/div[2]')
            opt2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/button/div[2]')
            opt3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[3]/button/div[2]')
            opt4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[4]/button/div[2]')
            optlist = [opt1.text, opt2.text, opt3.text, opt4.text]
            if question.text in words:
                questionindex = words.index(question.text)
                answer = definitions[questionindex]
            elif question.text in definitions:
                questionindex = definitions.index(question.text)
                answer = words[questionindex]
            correctopttemp = optlist.index(answer)
            correctopt = correctopttemp + 1
            actions = ActionChains(driver)
            actions.send_keys(correctopt)
            actions.perform()
            sleep(2)
    except NoSuchElementException:
        sleep(2)
        if todo == done:
            print(f'Reviewed {toreview} words, FININSHED')
            break
        elif done < todo:
            done += 1
            print(f'Reviewed {done * 100}, continuing...')
            driver.get(f'https://app.memrise.com/aprender/speed?course_id={courseid}')
            sleep(6)
