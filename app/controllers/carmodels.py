from app.database import data
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('brand', required=True)
parser.add_argument('model', required=True)
parser.add_argument('price', required=True, type=int)


class CarModels(Resource):
    def get(self):
        return data['carmodels']

    def post(self):
        args = parser.parse_args()
        # Increment the largest current ID by one
        id = max(map(lambda car: car['id'], data['carmodels'])) + 1
        data['carmodels'].append({
            'id': id,
            'brand': args['brand'],
            'model': args['model'],
            'price': args['price'],
        })

        return data['carmodels'], 201
