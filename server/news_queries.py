# Small test for accessing the NYT API.

import requests
import time
import json


NYT_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

API_KEY = "eb7c9ef23d6343dbbb7ba47b1d760610"





def query_nyt(data):
    # Take a query, and return a JSON object
    # from the New York Times API.
    data['api-key'] = API_KEY
    r = requests.get(NYT_URL, params=data)
    return r.json()




if __name__ == '__main__':
    # Get a JSON testing document.

    payload = {
        'begin_date': 20121117,
        'end_date': 20121118
    }

    r = query_nyt(payload)
    print(r)
