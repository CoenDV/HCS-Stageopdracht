from models import InsurancePolicy, CustomerPolicy, db
import numpy as np

class InsuranceRepository:

    def save_customer_policy(customer_policy):
        db.session.add(customer_policy)
        db.session.commit()
        return customer_policy
    
    def get_customer_policies_from_customerid(id):
        return CustomerPolicy.query.filter_by(customer_id=id).all()
    

    ### INIT INSURANCE POLICIES ###
    def get_all():
        return InsurancePolicy.query.all()
    
    def get_by_id(id):
        return InsurancePolicy.query.get(id)

    def save(insurance_policy):
        db.session.add(insurance_policy)
        db.session.commit()
        return insurance_policy
    
    def delete(insurance_policy):
        db.session.delete(insurance_policy)
        db.session.commit()
        return insurance_policy
    
    def get_similar_policies(text_embedding, top_k=2, relevance_threshold=0.5):
        # text_embedding = text_embedding.flatten()

        # Create a query that finds the most similar insurance policies	
        results = db.session.query(InsurancePolicy) \
            .order_by(InsurancePolicy.embedding.max_inner_product(text_embedding)) \
            .filter(InsurancePolicy.embedding.max_inner_product(text_embedding) < 0.5) \
            .limit(2) \
            .all()
        
        # Print results with their similarity scores
        for result in results:
            embedding_array = np.array(result.embedding)  # Convert embedding to a numpy array
            similarity = np.dot(embedding_array, text_embedding)  # Calculate inner product
            print(f"ID: {result.id}, Title: {result.title}, Similarity: {similarity}")

        for result in results:
            result.embedding = result.embedding.tolist()
            
        return results