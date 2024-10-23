from models import Customer, db

class CustomerRepository:
    def get_all():
        return Customer.query.all()

    def save(customer):
        db.session.add(customer)
        db.session.commit()
        return customer

    def login(data):
        return Customer.query.filter_by(username=data['username'], password=data['password']).first()