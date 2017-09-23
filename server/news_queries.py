# Small test for accessing the NYT API.

import requests
import time
import json


NYT_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

API_KEY = "eb7c9ef23d6343dbbb7ba47b1d760610"





def query_nyt(data):
    data['api-key'] = API_KEY
    r = requests.get(url, params=data)
    return r.json()




if __name__ == '__main__':

    payload = {
        'begin_date': 20121117,
        'end_date': 20121118,
        'api-key': API_KEY
    }


    r = requests.get(NYT_URL, params=payload)
    # print(r.url)
    # print(r.status_code)
    # print(r)
    print(r.json())
