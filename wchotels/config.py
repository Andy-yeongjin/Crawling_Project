import configparser

config = configparser.ConfigParser()
config.read("./wchotels_data.ini")
dss = config['dss']

class Config(object):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    naver_id = dss["NAVER_ID"] 
    naver_secret = dss["NAVER_SECRET"]
    webhook_url1 = dss["WEBHOOK_URL1"]
    webhook_url2 = dss["WEBHOOK_URL2"]
    webhook_url3 = dss["WEBHOOK_URL3"]
