from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('brand', required=True)
parser.add_argument('model', required=True)
parser.add_argument('price', required=True, type=int)

with open('data.json') as raw:
    data = json.load(raw)['carshop']


# Helper for grabbing one item in a list where id matches
def get(id, list):
    next(filter(lambda item: item['id'] == id, list), None)


class Employees(Resource):
    def get(self):
        return data['employees']


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


class Sales(Resource):
    def get(self):
        employees = data['employees']
        cars = data['carmodels']
        sales = data['sales']

        def sales_map(sale):
            car = get(sale['carmodel_id'], cars)
            if car is None:
                return 0
            return car['price']

        def employee_map(employee):
            employee_sales = filter(
                lambda sale: sale['employee_id'] == employee['id'],
                sales
            )

            employee['sales'] = sum(map(sales_map, employee_sales))
            return employee

        return list(map(employee_map, employees))


api.add_resource(Employees, '/employees')
api.add_resource(CarModels, '/carmodels')
api.add_resource(Sales, '/total_sales')
