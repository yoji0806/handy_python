import requests
import json

# GET Rest-API example

url = "https://xxx"
payload = {}
headers = {'Authorization' : 'Basic xxxx'}

# asusume resonse.text is <str> type
response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

status_code = response.status_code

if(status_code == 200):
    response_json = json.loads(response.text)
    # if response includes Japanese characters, put "ensure_ascii=False"
    print(json.dumps(response_json, indent=4, ensure_ascii=False))
else:
    print("error: status code: ", status_code)

