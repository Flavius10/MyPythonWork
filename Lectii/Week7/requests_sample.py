import json
import pprint
import requests


# GET all products
# response = requests.get("https://dummyjson.com/products")

# GET one product
response = requests.get("https://dummyjson.com/products/5000")

# POST to add a product
# url = "https://dummyjson.com/products/add"
# headers = {'Content-Type': 'application/json'}
# data = {"title": "new title"}
#
# response = requests.post(url, headers=headers, data=json.dumps(data))

# PATCH to update a product
# url = "https://dummyjson.com/products/1"
# headers = {'Content-Type': 'application/json'}
# data = {'title': 'iPhone 11', 'price': 749}
#
# response = requests.patch(url, headers=headers, data=json.dumps(data))

# DELETE a product
# url = "https://dummyjson.com/products/29"
#
# response = requests.delete(url)


if __name__ == "__main__":
    if response.status_code == 200:
        # deserializăm fișierul JSON
        json_data = response.json()
        pprint.pprint(json_data)
        # print(type(json_data))
        # pprint.pprint(json_data['products'][0])
    else:
        print("Cererea nu a fost îndeplinită cu succes. Cod de stare:", response.status_code)
