import json
import urllib.request

url = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'

token = 'AQAAAAAWfIrhAATv4xlw0S0uL0IGomtxiMQqhH4'

login = 'driver-acquisition'

data = {
    'method': 'GetClientInfo',
    'token': token,
    'locale': 'ru',
    'param': [login]
}

jdata = json.dumps(data, ensure_ascii=False).encode('utf-8')

response = urllib.request.urlopen(url, jdata)

print(response.read().decode('utf-8'))