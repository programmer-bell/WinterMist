# import requests

# endpoint = "http://127.0.0.1:8000/api/products/1/"

# # GET request 

# response = requests.get(endpoint)

# print("Status:", response.status_code)
# print("Response:", response.json())



import requests

endpoint = "http://127.0.0.1:8000/api/products/"

product_data = {
    "title": "New Product",
    "content": "Posted from Python client",
    "price": "49.99"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(endpoint, json=product_data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
