from app.models.sale import Sale
from app.models.employee import Employee
from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'sales': fields.Integer,
}


class Sales(Resource):
    @marshal_with(resource_fields)
    def get(self):
        employees = Employee.query.all()
        sales = Sale.query.join(Sale.car).all()

        ret = []

        for employee in employees:
            ret.append({
                'id': employee.id,
                'name': employee.name,
                'sales': sum(map(lambda sale: sale.car.price, filter(
                    lambda sale: sale.employee_id == employee.id,
                    sales
                )))
            })

        return ret
