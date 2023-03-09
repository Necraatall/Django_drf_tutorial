import requests

endpoint = "http://127.0.0.1:8080/api/"


get_response = requests.post(
    endpoint,
    json={
    "title": "trying post",
    "content": "Hello world",
    "price": "20.05",
    "my_discount": "300.56"
    })

print(get_response.json())
