from repositories.insuranerepository import InsuranceRepository
from models import InsurancePolicy, CustomerPolicy

class InsuranceService:

    def create_customer_policy(data):
        customer_policy = CustomerPolicy(
            customer_id = data['customer_id'],
            dateStart = data['dateStart'],
            pricePerMonth = data['pricePerMonth'],
            car_licenseplate = data['car_licenseplate'],
            insurancepolicy_id = data['insurancepolicy_id']
        )
        return InsuranceRepository.save(customer_policy)

    def get_customer_policies_from_customerid(id):
        return InsuranceRepository.get_customer_policies_from_customerid(id)

    ### INSURANCE POLICIES ###
    def create_insurance_policy(data):
        insurance_policy = InsurancePolicy(
            title = data['title'],
            insuranceType = data['insuranceType'],
            summary = data['summary'],
        )
        return InsuranceRepository.save(insurance_policy)
    
    def get_insurance_policy_by_id(id):
        return InsuranceRepository.get_by_id(id)
    
    def get_insurance_policies_by_customer_id(customer_id):
        return InsuranceRepository.get_by_customer_id(customer_id)
    
    def get_all_insurance_policies():
        return InsuranceRepository.get_all()
    
    def delete_insurance_policy(id):
        insurance_policy = InsuranceRepository.get_by_id(id)
        return InsuranceRepository.delete(insurance_policy)
    
