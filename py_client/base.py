# import requests

# endpoint = 'http://127.0.0.1:8000/api/'  # Enpoint for get or post data from the clinet

# # response = requests.get(endpoint,params={'abc':123}) # Endpoint to fetch data from api endpoint

# response = requests.post(endpoint,params={'abc':123}, json={"query": "Hello world"})

# print(response.json())


import requests

endpoint = "http://127.0.0.1:8000/api/"

product_data = {
    "title": "Hello World Product",
    "content": "Posted from Python client",
    "price": "49.99"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(endpoint, json=product_data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())

