from app import db


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    employee = db.relationship('Employee',
                               backref=db.backref('sales', lazy=True))
    car = db.relationship('Car',
                          backref=db.backref('cars', lazy=True))
