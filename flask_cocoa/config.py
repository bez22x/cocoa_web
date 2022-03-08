import os

os.environ['KAFKA_HOST'] = '127.0.0.1'
os.environ['KAFKA_PORT'] = '9093'
os.environ['KAFKA_TOPIC'] = 'TopicA'

os.environ['MYSQL_HOST'] = '18.180.227.212'
os.environ['MYSQL_PORT'] = '3306'
os.environ['MONGO_HOST'] = '35.73.202.11'
os.environ['MONGO_PORT'] = '27017'

mysql_host = os.environ.get('MYSQL_HOST', 'localhost')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'my-secret-pw')
mysql_db = os.environ.get('MYSQL_DB', 'tc_store_new')
mysql_port = os.environ.get('MYSQL_PORT', '3306')
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_password = os.environ.get('MONGO_PASSWORD', 'my-secret-pw')
mongo_db = os.environ.get('MONGO_DB', 'cocoa')
mongo_port = os.environ.get('MONGO_PORT', '27017')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'
MONGO_URI = f'mongodb://root:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_db}?authSource=admin'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'secret key'