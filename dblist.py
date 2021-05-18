from pymongo import MongoClient
client = MongoClient("mongodb://myUserAdmin:password@HOSTNAME:NODEPORT")
for db in client.list_databases():
    print(db)
