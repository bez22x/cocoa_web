## Cocoa Web


### connect to mongodb
mongo "mongodb://127.0.0.1:27017"

show dbs
use cocoa
show collections


docker run --name some-mongo -p 27017:27017 -v ${PWD}/db_storage/mongoDB:/data/db -d mongo