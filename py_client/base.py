import requests

endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/'

get_respone = requests.get(endpoint) # Basic API Request
print(get_respone.text) # Print raw text response 
