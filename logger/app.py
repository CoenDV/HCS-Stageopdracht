from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS

from src.logcontroller import controller

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Allow CORS for all domains on all routes
CORS(app)

app.register_blueprint(controller)

def create_tables():
    with app.app_context():
        db.create_all()	

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)