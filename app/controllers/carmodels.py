from app import db
from app.models.car import Car
from flask_restful import Resource, reqparse, fields, marshal_with

parser = reqparse.RequestParser()
parser.add_argument('brand', required=True)
parser.add_argument('model', required=True)
parser.add_argument('price', required=True, type=int)

resource_fields = {
    'id': fields.Integer,
    'brand': fields.String,
    'model': fields.String,
    'price': fields.Integer,
}


class CarModels(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Car.query.all()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        model = Car(brand=args['brand'], model=args['model'],
                    price=args['price'])

        db.session.add(model)
        db.session.commit()

        return Car.query.get(model.id), 201
