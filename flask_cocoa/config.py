import os

mysql_host = os.environ.get('MYSQL_HOST', 'localhost')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'tony17706')
mysql_db = os.environ.get('MYSQL_DB', 'tc_store_new')
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_db = os.environ.get('MONGO_DB', 'cocoa')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{mysql_password}@{mysql_host}:3306/{mysql_db}'
MONGO_URI = f'mongodb://{mongo_host}:27017/{mongo_db}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'secret key'