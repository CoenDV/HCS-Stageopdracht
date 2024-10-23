from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

from controllers.customercontroller import customer_bp
from controllers.carcontroller import car_bp
from controllers.insurancecontroller import insurance_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(customer_bp)
app.register_blueprint(car_bp)
app.register_blueprint(insurance_bp)

if __name__ == '__main__':
    app.run(debug=True)