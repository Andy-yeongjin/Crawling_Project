# import libs.rekey as rekey
from flask import *
import requests, json
import libs.slack as slack
from PIL import Image
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import requests
from scrapy.http import TextResponse
import re


urls_df = pd.read_csv('./urls.csv')
urls2_df = pd.read_csv('./urls2.csv')

app = Flask(__name__)

client = {"username": "root", "pw": "dss", "ip": "3.36.196.36"}

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{client["username"]}:{client["pw"]}@{client["ip"]}/dss'

mysql_db = SQLAlchemy(app)

class Hotels(mysql_db.Model):
    
    __tablename__ = 'hotels_total'
    
    index = mysql_db.Column(mysql_db.String(500), primary_key=True)
    name = mysql_db.Column(mysql_db.String(500), nullable=False)
    rating = mysql_db.Column(mysql_db.String(500), nullable=False)
    price = mysql_db.Column(mysql_db.String(500), nullable=False)
    service = mysql_db.Column(mysql_db.String(500), nullable=False)
    nearby = mysql_db.Column(mysql_db.String(500), nullable=False)
    
    
    def __init__(self, index, name, rating, price, service, nearby):
        self.index = index
        self.name = name
        self.rating = rating
        self.price = price
        self.service = service
        self.nearby = nearby
        
    
    def __repr__(self):
        return "<HOTEL {}, {}, {}, {}, {}>".format(self.name, self.rating, self.price, self.service, self.nearby)
    
from config import Config
Config.webhook_url1
Config.webhook_url2
Config.webhook_url3
request_url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {"X-Naver-Client-Id": Config.naver_id, "X-Naver-Client-Secret": Config.naver_secret}


@app.route('/jarvis', methods=['POST']) 
def jarvis(): 
    trigger_word = request.form.get('trigger_word')
    msg = request.form.get('text')
    msg = msg.replace(trigger_word, '').strip()
    slack.send_msg3('Hello sir')
    
    if msg[-4:] == 'adam':
        slack.send_msg3('Change optimizer to Adam')
        
    elif msg[-3:] == 'sgd':
        slack.send_msg3('Change optimizer to SGD')
        
    elif msg[-12:] == 'learningrate':
        slack.send_msg3(f'Change learningrate to {msg.split()[0]}')
        
    elif msg[-9:] == 'batchsize':
        slack.send_msg3(f'Change batchsize to {msg.split()[0]}')   
        
    elif msg[-6:] == 'epochs':
        slack.send_msg3(f'Change epochs to {msg.split()[0]}')
        
    elif msg[-4:] == 'name':
        slack.send_msg3(f'Change all names to {msg.split()[0]}')

        
    

@app.route('/LOTTE_City_Hotel_Myeongdong') 
def myimage2(): 
    return render_template("myimage2.html")

@app.route('/bot')
def index():
    return 'server is running'

@app.route('/like', methods=['POST'])
def like():
    trigger_word = request.form.get('trigger_word')
    msg = request.form.get('text')
    msg = msg.replace(trigger_word, '').strip()
    msg = msg.replace(' ', '')
    
    if msg[-2:] == '호텔':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']

        msg = msg.lower()
        msg = msg.replace('hotel', '')
        msg = msg.replace(' ','')
        # msg = msg.split(' ')[0]
        msg = msg.replace('-','')
        if msg == 'chosun':
            msg = 'josun'
        slack.send_msg2(msg)
        if len(msg) < 4 :
            slack.send_msg2('워드클라우드가 없는 호텔입니다 ^^')
            
        else:
            msg = urls2_df[urls2_df['urls'].str.contains(msg)]['urls']
            
            if len(msg) == 0 :
                slack.send_msg2('워드클라우드가 없는 호텔입니다 ^^')
            else:
                for i in range(0,len(msg.values)):
                    text = msg.values[i]
                    slack.send_msg2(text)
                    
    elif msg == '효정':
        slack.send_msg2('https://img.hankyung.com/photo/202105/BF.26464886.1.jpg')

    elif msg[-2:] == '정보':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']

        msg = msg.lower()
        msg = msg.replace('hotel', '')
        msg = msg.replace('about', '')
        msg = msg.replace('information', '')
        msg = msg.replace(' ','')
        #msg = msg.split(' ')[0]
        msg = msg.replace('-','')
       
        
        datas = Hotels.query.filter(Hotels.index.ilike(f'%{msg}%'))
        
        
        for i in range(0,100):
            try:
                slack.send_msg2(str(datas[i]))
            except:
                pass
    
    elif msg == '미국환율':
        url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
        req = requests.get(url)
        response = TextResponse(req.url, body=req.text, encoding='utf-8')
        USD = response.xpath('//*[@id="exchangeList"]/li[1]/a[1]/div/span[1]/text()').extract()[0]
        USD = float(re.sub(r',', '', USD))
        slack.send_msg2(f'현 시각 미국 환율은 $1 : ₩{USD} 입니다')
        
    elif msg[-2:] == '번역':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']
        msg = msg[:-11]
        slack.send_msg2(msg)
        
    elif msg[-9:] == 'translate':
        msg = msg[:-9]
        params = {"source": "en", "target": "ko", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']
        slack.send_msg2(msg)
        
    

@app.route('/dislike', methods=['POST'])
def dislike():
    trigger_word = request.form.get('trigger_word')
    msg = request.form.get('text')
    msg = msg.replace(trigger_word, '').strip()
    msg = msg.replace(' ', '')
    
    if msg[-2:] == '번역':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']
        msg = msg[:-11]
        slack.send_msg(msg)
        
    elif msg[-9:] == 'translate':
        msg = msg[:-9]
        params = {"source": "en", "target": "ko", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']
        slack.send_msg(msg)

    elif msg[-2:] == '정보':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']

        msg = msg.lower()
        msg = msg.replace('hotel', '')
        msg = msg.replace('about', '')
        msg = msg.replace('information', '')
        msg = msg.replace(' ','')
        #msg = msg.split(' ')[0]
        msg = msg.replace('-','')
        
        
        datas = Hotels.query.filter(Hotels.index.ilike(f'%{msg}%'))
        
        
        for i in range(0,100):
            try:
                slack.send_msg(str(datas[i]))
            except:
                pass
    
    
    elif msg[-2:] != '호텔':
        slack.send_msg('뒤에 호텔 혹은 번역을 붙여주세요 ^^')
    
    elif msg == '호텔':
        slack.send_msg('호텔 이름을 적어주세요 ^^')        
         
    elif msg[-2:] == '호텔':
        params = {"source": "ko", "target": "en", "text": msg}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        msg = result['message']['result']['translatedText']

        msg = msg.lower()
        msg = msg.replace('hotel', '')
        msg = msg.replace(' ','')
        msg = msg.replace('-','')
        if msg == 'chosun':
            msg = 'josun'
        slack.send_msg(msg)
        if len(msg) < 4 :
            slack.send_msg('워드클라우드가 없는 호텔입니다 ^^')
            
        else:
            msg = urls_df[urls_df['urls'].str.contains(msg)]['urls']
            
            if len(msg) == 0 :
                slack.send_msg('워드클라우드가 없는 호텔입니다 ^^')
            else:
                for i in range(0,len(msg.values)):
                    text = msg.values[i]
                    slack.send_msg(text)
    
    return Response(), 200

app.run(debug=True)
