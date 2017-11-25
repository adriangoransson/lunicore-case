from app import app, api

from app.controllers.employees import Employees
from app.controllers.carmodels import CarModels
from app.controllers.sales import Sales

api.add_resource(Employees, '/employees')
api.add_resource(CarModels, '/carmodels')
api.add_resource(Sales, '/total_sales')
