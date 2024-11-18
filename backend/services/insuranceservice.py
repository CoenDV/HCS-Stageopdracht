from repositories.insuranerepository import InsuranceRepository
from models import InsurancePolicy, CustomerPolicy
from sentence_transformers import SentenceTransformer

class InsuranceService:
    transformer = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/.cache')

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
    @classmethod
    def create_insurance_policy(cls, data):
        insurance_policy = InsurancePolicy(
            title = data['title'],
            content = data['content'],
            embedding = cls.transformer.encode(data['content']).tolist()
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
    
    @classmethod
    def get_similar_policies(cls, policy_text):
        text_embedding = cls.transformer.encode([policy_text])
        return InsuranceRepository.get_similar_policies(text_embedding)