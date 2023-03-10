import requests
from getpass import getpass

auth_endpoint = "http://localhost:8080/api/auth/"

username = input("What is Your username\n")
password = getpass("What is Your password\n")

auth_response = requests.post(
    auth_endpoint,
    json={'username': username, 'password': password})
print(auth_response.json())

# 'token': 'bdcaf54b012b8bbbff8abb6791ff072d1cbd0894'

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    # token = '1e01734dca6246b0f722566955d67469acbbdc1c'
    headers = {
        "Authorization": f'Token {token}'
    }
    endpoint = "http://localhost:8080/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
