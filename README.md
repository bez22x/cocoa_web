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
docker run --name some-mongo -p 27017:27017 -v ${PWD}/db_storage/mongoDB:/data/db -d mongo
```


## Reference:
* Mongo
  * CRUD
    * https://docs.mongodb.com/manual/tutorial/query-documents/
  * Flask-Pymongo
    * https://flask-pymongo.readthedocs.io/en/latest/