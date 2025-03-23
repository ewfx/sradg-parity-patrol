import requests

url = 'http://127.0.0.1:8000/data'
headers = {
    'accept': 'application/json'
}
params = {
    'name': 'Apple',
    'quant': 5
}

response = requests.post(url, headers = headers, params = params)

print(response.json())