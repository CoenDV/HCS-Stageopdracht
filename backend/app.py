from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS

from controllers.customercontroller import customer_bp
from controllers.carcontroller import car_bp
from controllers.insurancecontroller import insurance_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Allow CORS for all domains on all routes
CORS(app)

app.register_blueprint(customer_bp)
app.register_blueprint(car_bp)
app.register_blueprint(insurance_bp)

def create_tables():
    with app.app_context():
        db.create_all()	

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)