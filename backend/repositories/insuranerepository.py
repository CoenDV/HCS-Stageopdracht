from models import InsurancePolicy, db

class InsuranceRepository:
    def get_all():
        return InsurancePolicy.query.all()

    def save(insurance_policy):
        db.session.add(insurance_policy)
        db.session.commit()
        return insurance_policy

    def get_by_id(id):
        return InsurancePolicy.query.get(id)
    
    def get_by_customer_id(customer_id):
        return InsurancePolicy.query.filter_by(customer_id=customer_id).all()

    def delete(insurance_policy):
        db.session.delete(insurance_policy)
        db.session.commit()
        return insurance_policy