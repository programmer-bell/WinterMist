import requests

endpoint = 'http://127.0.0.1:8000/api/'  # Enpoint for get or post data from the clinet

response = requests.post(endpoint,params={'abc':123}, json={"query": "Hello world"})
print(response.json())

