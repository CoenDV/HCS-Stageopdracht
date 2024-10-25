from models import Car, InsurancePolicy, Customer, db

class CarRepository:
    def get_all():
        return Car.query.all()

    def save(car):
        db.session.add(car)
        db.session.commit()
        return car

    def get_by_licenseplate(licenseplate):
        return Car.query.get(licenseplate)

    def delete(car):
        db.session.delete(car)
        db.session.commit()
        return car
    
    def get_cars_from_customer(username):
        return db.session.query(Car).join(InsurancePolicy, Car.insurancepolicy_id == InsurancePolicy.id).join(Customer, InsurancePolicy.customer_id == Customer.id).all()