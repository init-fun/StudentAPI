import requests
import json

URL = "http://127.0.0.1:8000/"


def get_data(id=None):
    data = {}
    if id:
        data = {
            "id": id,
        }
    # convert id into JSON
    json_data = json.dumps(data)
    # sent it to homepage with the get request
    r = requests.get(url=URL, data=json_data)
    # we recieve the response in 'r'
    data = r.json()
    print(data)


get_data()
