import requests

# endpoint = 'https://httpbin.org/status/200'
# endpoint = 'https://httpbin.org/'
endpoint = 'http://127.0.0.1:8000/'

get_respone = requests.get(endpoint) # Basic API Request
print(get_respone.text) # Print raw text response 

