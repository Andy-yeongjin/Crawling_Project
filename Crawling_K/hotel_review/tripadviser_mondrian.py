from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 
import re 
import json
from selenium.webdriver.common.keys import Keys
import requests
from pandas import json_normalize

#TripAdviser

url = "https://www.tripadvisor.co.kr/Hotel_Review-g294197-d20886229-Reviews-Mondrian_Seoul_Itaewon-Seoul.html"


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

normal_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[3]/label')
bad_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[4]/label')
worst_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[5]/label')

# 3점 이하 평점 선택

try:
    normal_button.click()
except:
    pass
try:
    bad_button.click()
except:
    pass
try:
    worst_button.click()
except:
    pass

reviews = []

button2 = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[8]/div/div/a[1]')
button3 = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[8]/div/div/a[2]')


review = driver.find_elements_by_xpath('//*[@id="component_14"]/div/div[3]/div/div/div[3]/div[1]/div[1]/q/span')
for i in range(0,len(review)):
    reviews.append(review[i].text)

# 셀레니움 종료 
driver.quit()

# .txt 파일 저장
with open('ad_mondrian.txt', 'w') as f:
    for line in reviews:
        f.write(line)