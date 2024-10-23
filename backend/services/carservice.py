from repositories.carrepository import CarRepository
from models import Car

class CarService:
    def get_all_cars():
        return CarRepository.get_all()

    def create_car(data):
        car = Car(
            licensePlate=data['licensePlate'],
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            currentValue=data['currentValue'],
            insurancepolicy_id=data['insurancepolicy_id']
        )
        return CarRepository.save(car)

    def get_car_by_id(id):
        return CarRepository.get_by_id(id)

    def delete_car(id):
        car = CarRepository.get_by_id(id)
        return CarRepository.delete(car)