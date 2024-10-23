from flask import Blueprint, request, jsonify
from services.customerservice import CustomerService

customer_bp = Blueprint('customer_bp', __name__)

# TEST METHOD
@customer_bp.route('/customers', methods=['GET'])
def get_all_customers():
    customers = CustomerService.get_all_customers()
    return jsonify([customer.to_dict() for customer in customers])

# TEST METHOD
@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = CustomerService.create_customer(data)
    return jsonify(new_customer.to_dict()), 201

@customer_bp.route('/customers/login', methods=['POST'])
def login():
    data=request.get_json()
    customer = CustomerService.login(data)
    if customer is None:
        return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify(customer.to_dict()), 200
