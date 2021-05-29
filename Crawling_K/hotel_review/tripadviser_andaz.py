# 패키지 불러오기 
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

# 리뷰 첫페이지 크롤링 

## 리뷰 리스트에 저장 
reviews = []

## 리뷰 첫 페이지 url
url = "https://www.tripadvisor.co.kr/Hotel_Review-g294197-d17784746-Reviews-or-Andaz_Seoul_Gangnam-Seoul.html"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(2)

# 리뷰 점수 버튼 설정 
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
normal_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[3]/label')
bad_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[4]/label')
worst_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[5]/label')

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

review = driver.find_elements_by_xpath('//*[@id="component_14"]/div/div[3]/div/div/div[3]/div[1]/div[1]/q/span')

for i in range(0,len(review)):
    reviews.append(review[i].text)

# 리뷰페이지 전체 크롤링
for i in range(5, 1000, 5):
    url = f"https://www.tripadvisor.co.kr/Hotel_Review-g294197-d17784746-Reviews-or{i}-Andaz_Seoul_Gangnam-Seoul.html"
    driver.get(url)

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    normal_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[3]/label')
    bad_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[4]/label')
    worst_button = driver.find_element_by_xpath('//*[@id="component_14"]/div/div[3]/div[1]/div[1]/div[1]/ul/li[5]/label')
    

    review = driver.find_elements_by_xpath('//*[@id="component_14"]/div/div[3]/div/div/div[3]/div[1]/div[1]/q/span')
    
    if not review:
        break
        
    for i in range(0,len(review)):
        reviews.append(review[i].text)

print('done')

# 크롬드라이버 종료 
driver.quit()

# txt 파일 저장 
with open('ad_andaz.txt', 'w') as f:
    for line in reviews:
        f.write(line)