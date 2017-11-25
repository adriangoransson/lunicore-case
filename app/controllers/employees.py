from app.database import data
from flask_restful import Resource


class Employees(Resource):
    def get(self):
        return data['employees']
