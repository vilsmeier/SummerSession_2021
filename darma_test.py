import datetime
import time
import requests
import json
import pandas as pd
from pandas import DataFrame as df
import DogService as ds

API_ENDPOINT = "https://api.darma.cn/mattress/user/authorize"
TOKEN = "8b13b8eb9bf943f7832eacb6419f0cca"

#request Token
# request_accessToken = {"username":"sustech","password":"Sustech"}
# headers = {'content-type': 'application/json'}
# response_accessToken = requests.post(url = API_ENDPOINT, data = json.dumps(request_accessToken), headers = headers)
# token = pd.read_json(response_accessToken.content)['successData']['accessToken']
# print(type(response_accessToken.content))

#-----------#

#get current data

API_getCurrentData = "https://api.darma.cn/mattress/device/physiology/actual"
Headers = {'content-type':'application/json','accessToken':TOKEN}



def query(device_id = "612108000004"):
    request_currentData = {"deviceNos":device_id}
    r = requests.post(url = API_getCurrentData, data = json.dumps(request_currentData), headers = Headers)
    r = r.json()
    #deviceStatus = 
    # dic = json.load(r.content.json())
    dic = r['successData'][0]
    dic['markTime'] =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dic['markTime']))
    return {'heart':dic['heart'],
            'breath':dic['breath'],
            'motion':dic['motion'],
            'time':dic['markTime']}

time_cache = query()['time']
for i in range(99999):
    qr = query()
    if time_cache != qr['time']:
        ds.add_heart_rate(2,qr['heart'])
        time_cache = qr['time']
    print('\r','running #',i,end="",flush=True)
