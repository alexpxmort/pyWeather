import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/weather_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv('OPENWEATHER_API_KEY', '6c85e3c956dfcaeeb4a7e0c5a419f0d1')
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
