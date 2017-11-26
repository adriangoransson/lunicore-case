import json
from app import db, app
from app.models import *

with open('data.json') as raw:
    data = json.load(raw)['carshop']

print('Database URI: {}'.format(app.config['SQLALCHEMY_DATABASE_URI']))
print('This will drop and recreate tables and insert data.')
input('Press enter to continue or CTRL-C to quit. ')

print('Dropping tables')
db.drop_all()

print('Creating tables')
db.create_all()

print('Inserting employees')
for e in data['employees']:
    model = employee.Employee(id=e['id'], name=e['name'])
    db.session.add(model)

print('Inserting cars')
for c in data['carmodels']:
    model = car.Car(id=c['id'], brand=c['brand'], model=c['model'],
                    price=c['price'])
    db.session.add(model)

print('Inserting sales')
for s in data['sales']:
    model = sale.Sale(id=s['id'], employee_id=s['employee_id'],
                      car_id=s['carmodel_id'])
    db.session.add(model)

db.session.commit()
print('Reset complete')
