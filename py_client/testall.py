# # PUT Method calling by the client

# import requests

# pk = 3
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/update/"

# update_data = {
#     "title": "Updated Title",
#     "content": "Updated via Python client",
#     "price": "59.99"
# }

# response = requests.put(endpoint, json=update_data)
# print("Status:", response.status_code)
# print("Response:", response.json())


# # PATCH Method calling by the client
# import requests

# pk = 3
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/update/"

# patch_data = {
#     "title": "Patched Title Only"
# }

# response = requests.patch(endpoint, json=patch_data)
# print("Status:", response.status_code)
# print("Response:", response.json())


# # DELETE API 
# import requests

# pk = 3
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/delete/"

# response = requests.delete(endpoint)
# print("Status:", response.status_code)
# print("Deleted:", response.status_code == 204)



# import requests

# pk = 5
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/"

# response = requests.get(endpoint)
# print("Status:", response.status_code)
# print("Response:", response.json())


# import requests

# pk = 5
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/"

# update_data = {
#     "title": "Updated Title",
#     "content": "Fully updated product",
#     "price": "79.99"
# }

# response = requests.put(endpoint, json=update_data)
# print("Status:", response.status_code)
# print("Response:", response.json())


# import requests

# pk = 5
# endpoint = f"http://127.0.0.1:8000/api/products/{pk}/"

# patch_data = {
#     "title": "Partially Updated Title"
# }

# response = requests.patch(endpoint, json=patch_data)
# print("Status:", response.status_code)
# print("Response:", response.json())


import requests

pk = 5
endpoint = f"http://127.0.0.1:8000/api/products/{pk}/"

response = requests.delete(endpoint)
print("Status:", response.status_code)
print("Deleted:", response.status_code == 204)
