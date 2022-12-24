import requests
import json

url = "http://127.0.0.1:3000/telegram/login-bot-request/"

payload = json.dumps({
  "bot_token": "5441210926:AAEIEO-xBalcs5XlUZD1gOVKav3HbdqjlTo",
  "client_session_name": "ss",
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)