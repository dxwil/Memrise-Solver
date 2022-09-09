courseid = 
PATH = ''



import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
driver = webdriver.Chrome(PATH)

j = open('memrise.json', mode='w')


level = 1
no15 = 0
no14 = 0
no13 = 0
levelstr = str(level)

memrisedict = {'levels': {}}

while True:
    #has to be + 1 to the total levels
    if level == 338:
        json.dump(memrisedict, j)

        driver.quit()
        break
    else:
        driver.get(f'https://app.memrise.com/course/{courseid}/5000-words-top-87-sorted-by-frequency/{level}/')

        word1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[4]/div[3]/div')
        desc1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[4]/div[4]/div')
        word2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[5]/div[3]/div')
        desc2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[5]/div[4]/div')
        word3 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[6]/div[3]/div')
        desc3 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[6]/div[4]/div')
        word4 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[7]/div[3]/div')
        desc4 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[7]/div[4]/div')
        word5 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[8]/div[3]/div')
        desc5 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[8]/div[4]/div')
        word6 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[9]/div[3]/div')
        desc6 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[9]/div[4]/div')
        word7 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[10]/div[3]/div')
        desc7 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[10]/div[4]/div')
        word8 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[11]/div[3]/div')
        desc8 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[11]/div[4]/div')
        word9 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[12]/div[3]/div')
        desc9 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[12]/div[4]/div')
        word10 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[13]/div[3]/div')
        desc10 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[13]/div[4]/div')
        word11 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[14]/div[3]/div')
        desc11 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[14]/div[4]/div')
        word12 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[15]/div[3]/div')
        desc12 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[15]/div[4]/div')
        try:
            word13 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[16]/div[3]/div')
            desc13 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[16]/div[4]/div')
        except NoSuchElementException:
            no13 = no13 + 1
            pass
        try:
            word14 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[17]/div[3]/div')
            desc14 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[17]/div[4]/div')
        except NoSuchElementException:
            no14 = no14 + 1
            pass
        try:
            word15 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[18]/div[3]/div')
            desc15 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[18]/div[4]/div')
        except NoSuchElementException:
            no15 = no15 + 1
            pass
        try:
            word16 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[19]/div[3]/div')
            desc16 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[19]/div[4]/div')
        except NoSuchElementException:
            pass
        levelstr = str(level)
        memrisedict1 = {levelstr: {'words': [word1.text, word2.text, word3.text, word4.text, word5.text, word6.text, word7.text, word8.text, word9.text, word10.text, word11.text, word12.text], 'definitions': [desc1.text, desc2.text, desc3.text, desc4.text, desc5.text, desc6.text, desc7.text, desc8.text, desc9.text, desc10.text, desc11.text, desc12.text]}}
        #memrisedict['levels'][levelstr]['words'] = word1.text, word2.text, word3.text, word4.text, word5.text, word6.text, word7.text, word8.text, word9.text, word10.text, word11.text, word12.text
        #memrisedict['levels'][levelstr]['definitions'] = desc1.text, desc2.text, desc3.text, desc4.text, desc5.text, desc6.text, desc7.text, desc8.text, desc9.text, desc10.text, desc11.text, desc12.text
        memrisedict['levels'].update(memrisedict1)

        
        
        #memrisedict1 = {levelstr: {}}
        #memrisedict2 = {'words': [], 'definitions': []}
        
        #memrisedict['levels'].append(memrisedict1)
        #memrisedict['levels'][levelstr].append(memrisedict2)
        
        #memrisedict['levels'][levelstr]['words'] = word1.text, word2.text, word3.text, word4.text, word5.text, word6.text, word7.text, word8.text, word9.text, word10.text, word11.text, word12.text
        #memrisedict['levels'][levelstr]['definitions'] = (desc1.text, desc2.text, desc3.text, desc4.text, desc5.text, desc6.text, desc7.text, desc8.text, desc9.text, desc10.text, desc11.text, desc12.text)



        try:

            memrisedict['levels'][levelstr]['words'].append(word13.text)
            memrisedict['levels'][levelstr]['definitions'].append(desc13.text)


        except StaleElementReferenceException:
            print(f'no13 is {no13}')
            pass
        try:
            memrisedict['levels'][levelstr]['words'].append(word14.text)
            memrisedict['levels'][levelstr]['definitions'].append(desc14.text)
        except StaleElementReferenceException:
            print(f'no14 is {no14}')
            pass
        try:
            memrisedict['levels'][levelstr]['words'].append(word15.text)
            memrisedict['levels'][levelstr]['definitions'].append(desc15.text)
        except StaleElementReferenceException:
            print(f'no15 is {no15}')
            pass
        try:
            memrisedict['levels'][levelstr]['words'].append(word16.text)
            memrisedict['levels'][levelstr]['definitions'].append(desc16.text)
        except (NameError, StaleElementReferenceException):
            pass
        level = level + 1

        
#{"levels": { "98" :{  "words": ["blah", "blah"], "definitions": ["la", "la"]}, }}