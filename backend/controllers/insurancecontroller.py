from flask import Blueprint, request, jsonify
from services.insuranceservice import InsuranceService

insurance_bp = Blueprint('insurance_bp', __name__)

@insurance_bp.route('/customer_policies', methods=['POST'])
def create_customer_policy():
    data = request.get_json()
    new_customer_policy = InsuranceService.create_customer_policy(data)
    return jsonify(new_customer_policy.to_dict()), 201

@insurance_bp.route('/customer_policies/<int:id>', methods=['GET'])
def get_customer_policies_from_customerid(id):
    customer_policies = InsuranceService.get_customer_policies_from_customerid(id)
    return jsonify([customer_policy.to_dict() for customer_policy in customer_policies])



### INIT INSURANCE POLICIES ###
@insurance_bp.route('/insurance_policies', methods=['POST'])
def create_insurance_policy():
    data = request.get_json()
    new_insurance_policy = InsuranceService.create_insurance_policy(data)
    return jsonify(new_insurance_policy.to_dict()), 201

@insurance_bp.route('/insurance_policies', methods=['GET'])
def get_all_insurance_policies():
    insurance_policies = InsuranceService.get_all_insurance_policies()
    return jsonify([insurance_policy.to_dict() for insurance_policy in insurance_policies])

@insurance_bp.route('/insurance_policies/<int:id>', methods=['DELETE'])
def delete_insurance_policy(id):
    insurance_policy = InsuranceService.delete_insurance_policy(id)
    return jsonify(insurance_policy.to_dict()), 200


@insurance_bp.route('/insurance_policies/<int:id>', methods=['GET'])
def get_insurance_policy_by_id(id):
    insurance_policy = InsuranceService.get_insurance_policy_by_id(id)
    if insurance_policy is None:
        return jsonify({'error': 'Insurance policy not found'}), 404
    return jsonify(insurance_policy.to_dict()), 200

@insurance_bp.route('/insurance_policies/customer/<int:customer_id>', methods=['GET'])
def get_insurance_policies_by_customer_id(customer_id):
    insurance_policies = InsuranceService.get_insurance_policies_by_customer_id(customer_id)
    return jsonify([insurance_policy.to_dict() for insurance_policy in insurance_policies])