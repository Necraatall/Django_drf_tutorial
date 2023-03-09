import requests

endpoint = "http://127.0.0.1:8080/api/products/"

data={
    "title": "this field id done"
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())
