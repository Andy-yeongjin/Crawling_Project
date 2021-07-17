# -*- coding: utf8 -*- 
import requests
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
import re 
import json
import csv
import random
import nltk
from PIL import Image
from konlpy.corpus import kobill
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager, rc
from wordcloud import ImageColorGenerator
import numpy as np
# plt.rcParams['axes.unicode_minus'] = False

# f_path = '/Library/Fonts/Arial Unicode.ttf'
# font_name = font_manager.FontProperties(fname=f_path).get_name()

# rc('font', family=font_name)
import platform
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

# 우분투 환경, 한글
plt.rcParams['axes.unicode_minus'] = False

# path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
# font_name = font_manager.FontProperties(fname=path).get_name()
# rc('font', family='NanumBarunGothic')

def grey_color_func(**kwarg):
    return 'hsl(0, 0%%, %d%%)' % random.randint(60,100)


with open('naver_hotels_links.csv', 'r', encoding='utf-8') as f: 
    rdr = csv.reader(f) 
    for line in rdr:
        links = line


number = 0

for link in links[1601:2400]:
    print(number)
    number += 1

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1024x600')
    driver = webdriver.Chrome(options=options)

    driver.get(link)
    time.sleep(5)

    try:
        language = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[4]/div[1]')
        language.click()
        time.sleep(1)
        language_ko = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[4]/div[1]/ul/li[2]')
        language_ko.click()
        time.sleep(1)
    except:
        print('no_review')
        pass

    pro = []
    pros = []
    prev_user = None

    while True:
        try:
            pro = driver.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/ul/li/div[2]/div[1]/div/span[2]/em[2]')
        except:
            pass


        if pro == []:
            break

        curr_user2 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/ul/li[1]/div[3]/span[5]')
        curr_user = curr_user2.text

        if curr_user == prev_user:
            print('Done')
            break

        else:
            prev_user = curr_user

        for i in pro:
            pros.append(i.text)
        
        try:
            next_button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[5]/a[2]')
            next_button.click()
            time.sleep(3)
        except:
            print('no_more_reviews')


    try:
        other_button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[6]/ul/li[2]/a')
        other_button.click()
        time.sleep(3)
        
        language = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[4]/div[1]')
        language.click()
        language_ko = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[4]/div[1]/ul/li[2]')
        language_ko.click()

        while True:
            try:
                pro = driver.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/ul/li/div[2]/div[1]/div/span[2]/em[2]')
            except:
                pass   

            if pro == []:
                break
            
            curr_user2 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/ul/li[1]/div[3]/span[5]')
            curr_user = curr_user2.text

            if curr_user == prev_user:
                print('Done2')
                break
                
            else:
                prev_user = curr_user

            for i in pro:
                pros.append(i.text)

            next_button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[@class="hotel_used_review ng-isolate-scope"]/div[2]/div[5]/a[2]')
            next_button.click()
            time.sleep(3)
    except:
        print('Pass')

    driver.quit() 

    name = link[50:][:-8]
    with open(f'./txtfiles/{name}.txt', 'w') as f:
            for line in pros:
                f.write(line)