import os

class Config:
    SECRET_KEY = os.environ.get('25ffc2509e9517a2f5142017d33c2a4b') 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@db:5432/moviecut'
    SQLALCHEMY_TRACK_MODIFICATIONS = False