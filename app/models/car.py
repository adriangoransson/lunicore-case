from app import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    model = db.Column(db.String(150), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<CarModel %r> ' % self.model
