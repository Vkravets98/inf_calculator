import requests

def client():
    return requests.post(
        'http://127.0.0.1:8000/human',
        {'id': 1,
         'name': 'Alex',
         'age': 20
    }
    ).text
print(client())