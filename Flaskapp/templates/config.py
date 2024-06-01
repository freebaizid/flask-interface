# myflaskpackage/templates/config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Flask-App.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
