import requests

endpoint = "http://127.0.0.1:8000/api/products/"

# product_data = {
#     "title": "New Product",
#     "content": "Posted from Python client",
#     "price": "49.99"
# }

# headers = {
#     "Content-Type": "application/json"
# }

response = requests.post(endpoint)

print("Status:", response.status_code)
print("Response:", response.json())

