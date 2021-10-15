import requests
import json
def fetch_data():
    response = requests.get('').text
    return response

while True:
    try:
        data = fetch_data()
        data_store = requests.post('url',data=json.dumps(data))
    except Exception as e:
        print('no data')