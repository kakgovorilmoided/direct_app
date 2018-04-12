'''import json, urllib2

url = 'https://api.direct.yandex.ru/v4/json/'

token = 'AQAAAAAj8JhYAATv4ueITCr7W0XtlqqlXkcK_48'

login = 'driver-acquisition'

data = {
   'method': 'GetClientInfo',
   'token': token,
   'locale': 'ru',
   'param': [login]
}

jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

response = urllib2.urlopen(url,jdata)

print response.read().decode('utf8')'''

# token: AQAAAAAWfIrhAATv4xlw0S0uL0IGomtxiMQqhH4

import json
import urllib.request
import urllib
import urllib.parse

url = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'

token = 'AQAAAAAWfIrhAATv4xlw0S0uL0IGomtxiMQqhH4'

login = 'driver-acquisition'

data = {
    'method': 'GetClientInfo',
    'token': token,
    'locale': 'eng',
    'param': [login],
}

data_byte = urllib.parse.urlencode(data).encode("utf-8")
req = urllib.request.Request(url)
with urllib.request.urlopen(req,data=data_byte) as f:
    resp = f.read()
    print(resp)


# curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns

