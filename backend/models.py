from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class InsuranceType(Enum):
    WA = 1
    WA_PLUS = 2
    ALL_RISK = 3

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    policies = db.relationship('InsurancePolicy', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.username}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username
        }

class InsurancePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    dateStart = db.Column(db.Date, nullable=False)
    pricePerMonth = db.Column(db.Float, nullable=False)  # Changed Double to Float
    insuranceType = db.Column(db.Enum(InsuranceType), nullable=False)  # Enum reference
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    car = db.relationship('Car', backref='insurancePolicy', lazy=True)

    def __repr__(self):
        return f'<InsurancePolicy {self.title}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "dateStart": self.dateStart.isoformat(),
            "pricePerMonth": self.pricePerMonth,
            "insuranceType": self.insuranceType.name,
            "customer_id": self.customer_id
        }

class Car(db.Model):
    licensePlate = db.Column(db.String(8), primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    currentValue = db.Column(db.Float, nullable=False)  # Changed Double to Float
    insurancepolicy_id = db.Column(db.Integer, db.ForeignKey('insurance_policy.id'))  # Add ForeignKey

    def __repr__(self):
        return f'<Car {self.brand} {self.model}>'
    
    def to_dict(self):
        return {
            "licensePlate": self.licensePlate,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "currentValue": self.currentValue,
            "insurancepolicy_id": self.insurancepolicy_id
        }