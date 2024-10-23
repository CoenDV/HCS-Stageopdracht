from models import Car, db

class CarRepository:
    def get_all():
        return Car.query.all()

    def save(car):
        db.session.add(car)
        db.session.commit()
        return car

    def get_by_id(id):
        return Car.query.get(id)

    def delete(car):
        db.session.delete(car)
        db.session.commit()
        return car