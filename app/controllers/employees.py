from app.models.employee import Employee
from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


class Employees(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Employee.query.all()
