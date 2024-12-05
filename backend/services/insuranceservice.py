from repositories.insuranerepository import InsuranceRepository
from models import InsurancePolicy, CustomerPolicy
from sentence_transformers import SentenceTransformer
import requests
import time
import socket

class InsuranceService:
    transformer = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/.cache')

    def create_customer_policy(data):
        customer_policy = CustomerPolicy(
            customer_id = data['customer_id'],
            date_start = data['date_start'],
            price_per_month = data['price_per_month'],
            car_licenseplate = data['car_licenseplate'],
            insurance_policy_id = data['insurance_policy_id']
        )
        return InsuranceRepository.save_customer_policy(customer_policy)

    def get_customer_policies_from_customerid(id):
        customer_policies = InsuranceRepository.get_customer_policies_from_customerid(id)
        for customer_policy in customer_policies:
            print(customer_policy.to_dict())
        return customer_policies

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
    def get_similar_policies(cls, data):
        text_embedding = cls.transformer.encode(data["text"]).tolist()
        return_data = InsuranceRepository.get_similar_policies(text_embedding)

        requests.post(
            "https://logger-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/backend_logs",
            json={
                "correlation_id": data["correlation_id"],
                "prompt": data["text"],
                "retrieved_documents": return_data["retrieved_documents"],
                "similarity_score": return_data["similarity_score"],
                "time": time.strftime("%H:%M:%S", time.localtime()),
                "url": socket.gethostbyname(socket.gethostname())
            }
        )

        return return_data["retrieved_documents"]