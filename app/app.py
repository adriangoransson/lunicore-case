from flask import Flask
from flask_restful import Api

from app.controllers.employees import Employees
from app.controllers.carmodels import CarModels
from app.controllers.sales import Sales

app = Flask(__name__)
api = Api(app)

api.add_resource(Employees, '/employees')
api.add_resource(CarModels, '/carmodels')
api.add_resource(Sales, '/total_sales')
