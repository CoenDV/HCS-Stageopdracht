from repositories.customerrepository import CustomerRepository
from models import Customer

class CustomerService:
    def get_all_customers():
        return CustomerRepository.get_all()

    def create_customer(data):
        customer = Customer(
            firstname=data['firstname'],
            lastname=data['lastname'],
            username=data['username'],
            password=data['password']
        )
        return CustomerRepository.save(customer)

    def login(data):
        return CustomerRepository.login(data)