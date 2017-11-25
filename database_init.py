import json
from app import db
from app.models import *

with open('data.json') as raw:
    data = json.load(raw)['carshop']

db.create_all()
for e in data['employees']:
    model = employee.Employee(id=e['id'], name=e['name'])
    db.session.add(model)

for c in data['carmodels']:
    model = car.Car(id=c['id'], brand=c['brand'], model=c['model'],
                    price=c['price'])
    db.session.add(model)

for s in data['sales']:
    model = sale.Sale(id=s['id'], employee_id=s['employee_id'],
                      car_id=s['carmodel_id'])
    db.session.add(model)

db.session.commit()
