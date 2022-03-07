## Cocoa Web


## Mongodb
* connect to mongodb
```sh
mongo "mongodb://127.0.0.1:27017"
```
* db operation command
```sh
show dbs
use cocoa
show collections
```
## Docker:
* Run MongoDB
```sh
docker run --name some-mongo -p 27017:27017 -v ${PWD}/db_storage/mongoDB/data:/data/db -d mongo
```
* Run Mysql
```sh
docker run -p 3307:3306 -v ${PWD}/db_storage/mysql/data:/var/lib/mysql --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d init-mysql
```

## Docker-Compose
```
docker-compose up
docker-compose down
```

pipenv lock -r > requirements.txt

## Reference:
* Mongo
  * CRUD
    * https://docs.mongodb.com/manual/tutorial/query-documents/
  * Flask-Pymongo
    * https://flask-pymongo.readthedocs.io/en/latest/