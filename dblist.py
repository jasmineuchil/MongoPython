from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://myUserAdmin:password@p1213-master.p1213.cecc.ihost.com:31466")
for db in client.list_databases():
    print(db)