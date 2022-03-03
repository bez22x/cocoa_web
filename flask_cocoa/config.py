import os

os.environ['MYSQL_PORT'] = '3308'
os.environ['MONGO_PORT'] = '27018'

mysql_host = os.environ.get('MYSQL_HOST', 'localhost')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'my-secret-pw')
mysql_db = os.environ.get('MYSQL_DB', 'tc_store_new')
mysql_port = os.environ.get('MYSQL_PORT', '3306')
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_db = os.environ.get('MONGO_DB', 'cocoa')
mongo_port = os.environ.get('MONGO_PORT', '27017')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'
MONGO_URI = f'mongodb://{mongo_host}:{mongo_port}/{mongo_db}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'secret key'