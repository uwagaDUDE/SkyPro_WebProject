import requests

def get_to_server():
    return requests.get('http://localhost:8080/')

print(get_to_server().text)