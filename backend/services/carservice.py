from repositories.carrepository import CarRepository
from models import Car

class CarService:
    def get_all_cars():
        return CarRepository.get_all()

    def create_car(data):
        car = Car(
            licenseplate=data['licenseplate'],
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            current_value=data['current_value'],
        )
        return CarRepository.save(car)

    def get_car_by_id(id):
        return CarRepository.get_by_id(id)

    def delete_car(licenseplate):
        car = CarRepository.get_by_licenseplate(licenseplate)
        print(car)
        return CarRepository.delete(car)
    
    def get_cars_from_customer(username):
        cars = CarRepository.get_cars_from_customer(username)
        return cars