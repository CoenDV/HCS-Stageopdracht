from flask import Blueprint, request, jsonify
from services.carservice import CarService

car_bp = Blueprint('car_bp', __name__)

@car_bp.route('/cars', methods=['GET'])
def get_all_cars():
    cars = CarService.get_all_cars()
    return jsonify([car.to_dict() for car in cars])

@car_bp.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    new_car = CarService.create_car(data)
    return jsonify(new_car.to_dict()), 201

@car_bp.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    car = CarService.get_car_by_id(id)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(car.to_dict()), 200

@car_bp.route('/customer/cars/<string:username>', methods=['GET'])
def get_cars_from_customer(username):
    cars = CarService.get_cars_from_customer(username)
    return jsonify([car.to_dict() for car in cars])