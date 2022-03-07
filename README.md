## Cocoa Web


## Mongodb
* connect to mongodb
```sh
mongo "mongodb://35.73.202.11:27017"
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
sudo docker run --name some-mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=my-secret-pw -p 27017:27017 -v ${PWD}/db_storage/mongoDB/data:/data/db -d mongo

```
* Run Mysql
```sh
docker run -p 3307:3306 -v ${PWD}/db_storage/mysql/data:/var/lib/mysql --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d init-mysql
```

* Run Flask
```shell
docker run -d -p 80:8080 -e MYSQL_HOST=10.0.1.48 -e MYSQL_PASSWORD=my-secret-pw -e MYSQL_DB=tc_store_new -e MONGO_HOST=10.0.1.130 -e MONGO_PASSWORD=my-secret-pw  -e MONGO_DB=cocoa cocoa-flask

```

* Run run model
```shell
docker run --rm -e MONGO_HOST=10.0.1.130 -e MYSQL_HOST=10.0.1.48 -v /home/ec2-user/flask/processing/run_model/data:/usr/src/app/data run-model
```
```shell
sudo systemctl start crond
sudo systemctl enable crond
crontab -e
0 0 * * MON
```
## Docker-Compose
```
docker-compose up
docker-compose down
```
```
移除 exited docker container
```
docker rm $(docker ps -a -f status=exited -q)
pipenv lock -r > requirements.txt

## Reference:
* Mongo
  * CRUD
    * https://docs.mongodb.com/manual/tutorial/query-documents/
  * Flask-Pymongo
    * https://flask-pymongo.readthedocs.io/en/latest/