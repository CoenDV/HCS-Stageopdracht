from repositories.insuranerepository import InsuranceRepository
from models import InsurancePolicy
from datetime import datetime

class InsuranceService:
    def get_all_insurance_policies():
        return InsuranceRepository.get_all()

    def create_insurance_policy(data):
        insurance_policy = InsurancePolicy(
            title=data['title'],
            dateStart=data['dateStart'],
            pricePerMonth=data['pricePerMonth'],
            insuranceType=data['insuranceType'],
            customer_id=data['customer_id']
        )
        return InsuranceRepository.save(insurance_policy)

    def get_insurance_policy_by_id(id):
        return InsuranceRepository.get_by_id(id)
    
    def get_insurance_policies_by_customer_id(customer_id):
        return InsuranceRepository.get_by_customer_id(customer_id)

    def delete_insurance_policy(id):
        insurance_policy = InsuranceRepository.get_by_id(id)
        return InsuranceRepository.delete(insurance_policy)