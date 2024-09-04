import requests

def get(l, w, url="http://localhost:8765/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': '11',
        'weight': '11',
    }

    response = requests.get('http://localhost:8765/fish', params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    return r