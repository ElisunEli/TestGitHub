import requests

url = "http://192.168.177.51/cm"
payload = {"cmnd": "Power TOGGLE"}

response = requests.post(url, params=payload)

print(response.text)