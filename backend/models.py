from flask_sqlalchemy import SQLAlchemy
from pgvector.sqlalchemy import Vector
from enum import Enum

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    policies = db.relationship('CustomerPolicy', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.username}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username
        }

class CustomerPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    dateStart = db.Column(db.Date, nullable=False)
    pricePerMonth = db.Column(db.Float, nullable=False) 
    
    car_licenseplate = db.Column(db.String(8), db.ForeignKey('car.licenseplate'), nullable=False)
    insurancepolicy_id = db.Column(db.Integer, db.ForeignKey('insurance_policy.id'), nullable=False)
    
    # Relationship to Car using the 'car_licenseplate' foreign key
    car = db.relationship('Car', backref='customer_policies', lazy=True)
    
    # Relationship to InsurancePolicy using the 'insurancepolicy_id' foreign key
    insurancepolicy = db.relationship('InsurancePolicy', backref='customer_policies', lazy=True)

    def __repr__(self):
        return f'<CustomerPolicy {self.customer_id} {self.insurancepolicy_id}>'
    
    def to_dict(self):
        # Include the related InsurancePolicy and Car objects
        car_dict = self.car.to_dict() if self.car else None
        insurance_policy_dict = self.insurancepolicy.to_dict() if self.insurancepolicy else None
        
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "insurance_policy": insurance_policy_dict,
            "car": car_dict,
            "dateStart": self.dateStart,
            "pricePerMonth": self.pricePerMonth
        }

class InsurancePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    embedding = db.Column(Vector(384), nullable=False)
    
    def __repr__(self):
        return f'<InsurancePolicy {self.title}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "embedding": self.embedding
        }

class Car(db.Model):
    licenseplate = db.Column(db.String(8), primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    currentValue = db.Column(db.Float, nullable=False)

    # Backref 'customer_policies' is already created by the relationship in CustomerPolicy
    def __repr__(self):
        return f'<Car {self.brand} {self.model}>'
    
    def to_dict(self):
        return {
            "licenseplate": self.licenseplate,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "currentValue": self.currentValue,
        }