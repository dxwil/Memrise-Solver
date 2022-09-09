#REQUIRMENTS:
#Python
#Selenium: pip3 install selenium
#Chrome
#chromedriver: https://chromedriver.chromium.org/
#Set words per session to 15

google_email = ''
google_pass = ''
PATH = ''




#Script start
todolevel = int(input('What level do you want to start with? '))
repeatamnttemp = int(input('How many levels do you want to do? '))
repeatamnt = repeatamnttemp * 2

repeatedamnt = 0

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
driver = webdriver.Chrome(PATH)

courseid = 47049
driver.get(f'https://app.memrise.com/aprender/learn?course_id={courseid}&level_index={todolevel}')
sleep(2)

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
sleep(7)

f = open('memrise.json')
data = json.load(f)

nextbtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[5]/button/div')
while True:
    nextbtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[5]/button/div')
    try:
        if nextbtn.text == "I don’t know":
            question = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[1]/h2')
            try:
                opt1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[1]/button/div[2]')
                opt2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]/button/div[2]')
                opt3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[3]/button/div[2]')
                opt4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[4]/button/div[2]')
                optlist = [opt1.text, opt2.text, opt3.text, opt4.text]
                typing = False
            except NoSuchElementException:
                typing = True
                pass
            levelstr = str(todolevel)
            if question.text in data['levels'][levelstr]['words']:
                questionindex = data['levels'][levelstr]['words'].index(question.text)
                answer = data['levels'][levelstr]['definitions'][questionindex]
            elif question.text in data['levels'][levelstr]['definitions']:
                questionindex = data['levels'][levelstr]['definitions'].index(question.text)
                answer = data['levels'][levelstr]['words'][questionindex]
            if typing is False:
                correctopttemp = optlist.index(answer)
                correctopt = correctopttemp + 1
                actions = ActionChains(driver)
                actions.send_keys(correctopt)
                actions.perform()
                sleep(0.5)
            elif typing is True:
                typedans = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div/input')
                typedans.send_keys(answer)
                sleep(2)
        elif nextbtn.text == 'Next':
            nextbtn.click()
    except StaleElementReferenceException as l:
        print(l)
        sleep(2)
        repeatedamnt + 1
        if repeatedamnt == repeatamnt:
            print(f'Completed {repeatedamnt} levels')
            break
        elif repeatedamnt < repeatamnt:
            todolevel1 = todolevel + 0.5
            if (todolevel1).is_integer() == False:
                pass
            elif (todolevel1).is_integer() == True:
                todolevel = todolevel1
            driver.get(f'https://app.memrise.com/aprender/learn?course_id={courseid}&level_index={todolevel}')
            sleep(2)