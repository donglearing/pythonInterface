import requests

url = "http://58.211.38.72:62080/backend/user/login"

payload = "{\n\"username\":\"super\",\n\"password\":\"Connext@0101\"\n}"
headers = { 'Content-Type': "application/json", 'cache-control': "no-cache"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)