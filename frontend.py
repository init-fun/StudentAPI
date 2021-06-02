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


def post_data(data):
    # py dict to JSON
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)


def update_data():
    data = {
        "id": 5,
        "name": "Haseeb",
        "city": "Bangalore",
    }

    # py dict to JSON
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)


def delete_data():
    data = {
        "id": 6,
    }

    # py dict to JSON
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)

    data = r.json()
    print(data)


data = {
    "name": "kapil",
    "city": "bengaluru",
    "roll": 10,
}

# get_data()
post_data(data)
# update_data()
# delete_data()


# get_data()
