from app.util import get
from app.database import data
from flask_restful import Resource
import copy


class Sales(Resource):
    def get(self):
        d = copy.deepcopy(data)
        employees = d['employees']
        cars = d['carmodels']
        sales = d['sales']

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
