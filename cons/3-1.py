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
import platform
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np


with open('naver_hotels_links.csv', 'r', encoding='utf-8') as f: 
    rdr = csv.reader(f) 
    for line in rdr:
        links = line

number = 1600

plt.rcParams['axes.unicode_minus'] = False
path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family='NanumBarunGothic')

for link in links[1600:2400]:
    name = link[50:][:-8]

    print(number)
    number += 1

    doc = open(f'./text/{name}.txt').read()
    mask = np.array(Image.open('./dislike.png'))
    image_color = ImageColorGenerator(mask)

    print('brought_t')

    try:
        t = Okt()
        tokens_ko = t.nouns(doc)

        ko = nltk.Text(tokens_ko)

        stop = ['호텔', '좀', '조금', '머리', '선택', '잠', '짐', '옆', '이용', '것', '안', '사용', '층', '방', '룸', '더', '정말', '점', '객실', '때', '수', '도', '신경', '부분', '생각', '곳', '하나', '물이', '아이', '내', '위', '듯', '다시', '줄', '느낌', '부분', '방이', '설치', '서울', '경우', '디', '시', '전혀', '때문', '등', '정도', '다른', '쪽', '알', '제공', '바로', '문의', '크게', '주변', '제', '그냥', '도로', '위', '막', '해', '아주', '이해', '분', '약간', '다음', '다른', '전', '함', '느낌', '처음', '매우', '번', '그', '꽤', '계속', '말씀', '크게', '진짜', '하나', '편이', '대한', '문제', '분', '또', '움', '확인', '자가', '관련', '두', '이', '그', '꼽자', '굳이', '거의', '모두', '구', '살짝', '굿', '날', '말', '객', '밤']

        ko = [each_word for each_word in ko if each_word not in stop]
        ko = nltk.Text(ko)

        data = ko.vocab().most_common(100)

        wordcloud = WordCloud(color_func=image_color, font_path=path, mask=mask, relative_scaling=0.2, background_color='black').generate_from_frequencies(dict(data))

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off'), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)

        plt.savefig(f'./wc3/{name}.jpg', 
                    bbox_inces='tight', 
                    pad_inches=0, 
                    dpi=100
                   )
        print(f'{name}done_worldcloud')

    except:
        print(f'{name}no_worldcloud')