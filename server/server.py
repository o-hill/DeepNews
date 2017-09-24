import sys
import numpy as np
from flask import Flask, request, abort
from time import time, sleep
from flask_restful import abort, Api, Resource, reqparse
from flask_cors import *
from serial import *
from news_queries import query_nyt


# -----------------------------------------------------------------------------


app = Flask(__name__)
api = Api(app)

valid_headers = ['Content-Type', 'Access-Control-Allow-Origin', '*']
cors = CORS(app, allow_headers=valid_headers)

#db = connect_to_database()

@app.route('/')
def hello_world():
    return "Hello World!"



class NewsQuery(Resource):

    def get(self):
        data = request.json
        data = deserialize(data)
        for k, v in data.items():
            print(str(k) + ": " + str(v))
        response = query_nyt(data)

        return serialize(response)

class TestJson(Resource):

    def get(self):
        data = open('./testData.json', 'r').read()
        data = data.replace("'", '"')
        print(data)
        return data





# -----------------------------------------------------------------------------

# Define API routes.

api.add_resource(NewsQuery, '/query', methods = ['GET'])
api.add_resource(TestJson, '/test', methods = ['GET'])




# -----------------------------------------------------------------------------




if __name__ == '__main__':
    # Launch the server!

    app.run(port=1492, debug=True)















# -----------------------------------------------------------------------------
