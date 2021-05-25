from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#Lists all the database
for db in client.list_databases():
    print(db)
