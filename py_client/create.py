import requests

endpoint = "http://localhost:8080/api/products/"

data={
    "title": "this field id done"
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())
