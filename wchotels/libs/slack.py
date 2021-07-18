import requests, json
from config import Config

WEBHOOK_URL = Config.webhook_url1
WEBHOOK_URL2 = Config.webhook_url2
WEBHOOK_URL3 = Config.webhook_url3

def send_msg(msg):
    payload = {'channel' : '#일반', 'username' : 'dislike', 'text' : msg}
    return requests.post(WEBHOOK_URL, json.dumps(payload))

def send_msg2(msg):
    payload = {'channel' : '#일반', 'username' : 'like', 'text' : msg}
    return requests.post(WEBHOOK_URL2, json.dumps(payload))

def send_msg3(msg):
    payload = {'channel' : '#일반', 'username' : 'Jarvis', 'text' : msg}
    return requests.post(WEBHOOK_URL3, json.dumps(payload))
