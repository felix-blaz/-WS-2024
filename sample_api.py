from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId


app = Flask(__name__)
api = Api(app)

class GetProducts(Resource):

    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data
        results = dumps(collection.find())
        return json.loads(results)

class GetTitles(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data
        results = dumps(collection.find({"ProductId": 3}))

        print(results)
        print(type(results))
        return json.loads(results)

             
api.add_resource(GetProducts, '/getProducts')
api.add_resource(GetTitles, '/getTitles')



            
if __name__ == '__main__':
    app.run(debug=True)
