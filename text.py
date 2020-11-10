import requests
import json

url = "https://age-of-empires-2-api.herokuapp.com/api/v1/unit/1"

payload  = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

