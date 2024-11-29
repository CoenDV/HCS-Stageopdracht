class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://HCSuser:HCSpassword@postgresql:5432/logs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False