from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import graphene
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://root:example@localhost:27017/")
db = client.sales
collection = db.sales_data
API_KEY = "aaa"

class GetProducts(Resource):

    def get(self):
        results = dumps(collection.find())
        return json.loads(results)


class Sale(graphene.ObjectType):
    Title = graphene.String()


class Query(graphene.ObjectType):
    titles = graphene.List(graphene.String)

    def resolve_titles(root, info):
        results = collection.find()
        titles = [item['Title'] for item in results]
        return titles


schema = graphene.Schema(query=Query)


class GetTitles(Resource):
    def get(self):
        result = schema.execute('{ titles }')
        data_json = json.dumps(result.data)
        return data_json

class InsertProducts(Resource):
    def post(self):
        # Check if API key is provided in the request URL
        api_key = request.args.get('api_key')
        if api_key != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 401

        # Parse request data
        data = request.json
        product_id = data.get('ProductId')
        title = data.get('Title')
        quantity = data.get('Quantity')

        # Validate request data
        if not all([product_id, title, quantity]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Store data in MongoDB
        try:
            product = {
                'ProductId': product_id,
                'Title': title,
                'Quantity': quantity
            }
            result = collection.insert_one(product)
            return jsonify({'message': 'Product added successfully', 'inserted_id': str(result.inserted_id)}), 201
        except Exception as e:
            return jsonify({'error': f'Failed to insert product: {str(e)}'}), 500



class Root(Resource):
    def get(self):
        endpoints = {
            '/getProducts': 'Will retrieve all the products in the mongo db\n',
            '/insertProducts': 'Will allow the user to add items into the momgo database as long as they have the api key. '
                               'This is done using postman\n',
            '/getTitles': 'Will allow the user to retrieve all the titles of the products in the database using graphql'
        }

        return jsonify(endpoints)

api.add_resource(Root, '/')
api.add_resource(InsertProducts, '/insertProducts')
api.add_resource(GetProducts, '/getProducts')
api.add_resource(GetTitles, '/getTitles')

if __name__ == '__main__':
    app.run(debug=True)