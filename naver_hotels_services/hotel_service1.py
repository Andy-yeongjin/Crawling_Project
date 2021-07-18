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

path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family='NanumBarunGothic')


with open('naver_hotels_links.csv', 'r', encoding='utf-8') as f: 
    rdr = csv.reader(f) 
    for line in rdr:
        links = line

number = 0

for link in links[0:800]:
    print(number)
    number += 1

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1024x600')
    driver = webdriver.Chrome(options=options)

    driver.get(link)
    time.sleep(5)

    try:
        hotel_name = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/strong').text
    except:
        print('no hotel name')

    try:
        hotel_rate = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/span').text
    except:
        print('no hotel rate')
        hotel_rate = None

    try:
        price = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/strong').text
    except:
        print('no hotel price')
        price = None

    try:
        service = driver.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div[7]/div[2]/dl')[0].text
        service = service.replace('\n', ', ')
    except:
        print('no hotel service')
        service = None
        
    try:
        nearby = driver.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div[8]/div[2]')[0].text
        nearby = nearby.replace('\n', ', ')
        nearby = nearby.replace('km', 'km - ')
    except:
        print('no nearby')
        nearby = None

    driver.quit()

    name = link[50:][:-8]
    name = name.lower()
    name = name.replace('_','')

    try:
        df = pd.DataFrame({'name':hotel_name, 'rating':hotel_rate, 'price':price, 'service': service, 'nearby':nearby}, index=[f'{name}'])

        df.reset_index(inplace=True)

        import configparser
        config = configparser.ConfigParser()

        import pymysql
        from sqlalchemy import create_engine
        pymysql.install_as_MySQLdb()
        import MySQLdb

        engine = create_engine("mysql+mysqldb://root:ID@IP/PW", encoding='utf8')
        conn = engine.connect()

        df.to_sql(name="hotels", con=engine, index=False, if_exists='append')
        print(f'{name} df')
    except:
        print(f'no {name} df')
        