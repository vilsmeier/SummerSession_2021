print("Hello world")

import requests
import json
import pandas as pd
from pandas import DataFrame as df

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
request_currentData = {"deviceNos":"612108000004"}
r = requests.post(url = API_getCurrentData, data = json.dumps(request_currentData), headers = Headers)
r = r.json()
#deviceStatus = 
# dic = json.load(r.content.json())
(r['successData'][0])



API_getSleepingReport = "https://api.darma.cn/mattress/v2/device/641938001790/sleep-report/20201101"
Headers = {'content-type':'application/json','accessToken':TOKEN}
request_currentData = {"deviceNos":"612108000004",'date':'20210811'}
r = requests.post(url = API_getCurrentData, data = json.dumps(request_currentData), headers = Headers)
r = r.json()

print(r)


