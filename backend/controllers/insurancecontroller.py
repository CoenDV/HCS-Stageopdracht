from flask import Blueprint, request, jsonify
from services.insuranceservice import InsuranceService

insurance_bp = Blueprint('insurance_bp', __name__)

@insurance_bp.route('/insurance_policies', methods=['GET'])
def get_all_insurance_policies():
    insurance_policies = InsuranceService.get_all_insurance_policies()
    return jsonify([insurance_policy.to_dict() for insurance_policy in insurance_policies])

@insurance_bp.route('/insurance_policies', methods=['POST'])
def create_insurance_policy():
    data = request.get_json()
    new_insurance_policy = InsuranceService.create_insurance_policy(data)
    return jsonify(new_insurance_policy.to_dict()), 201

@insurance_bp.route('/insurance_policies/<int:id>', methods=['GET'])
def get_insurance_policy_by_id(id):
    insurance_policy = InsuranceService.get_insurance_policy_by_id(id)
    if insurance_policy is None:
        return jsonify({'error': 'Insurance policy not found'}), 404
    return jsonify(insurance_policy.to_dict()), 200