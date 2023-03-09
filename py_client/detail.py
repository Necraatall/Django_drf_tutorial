import requests

endpoint = "http://127.0.0.1:8080/api/products/1/"


get_response = requests.get(
    endpoint)
    # json={
    # "title": "trying post",
    # "content": "Hello world",
    # "price": "trying price"
    # })

print(get_response.json())
