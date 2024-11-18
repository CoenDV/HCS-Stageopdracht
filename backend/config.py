class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://HCSuser:HCSpassword@localhost:5432/hcsinsurance'
    SQLALCHEMY_TRACK_MODIFICATIONS = False