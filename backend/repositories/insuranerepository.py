from models import InsurancePolicy, CustomerPolicy, db

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