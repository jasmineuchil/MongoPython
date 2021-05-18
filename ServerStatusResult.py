from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://myUserAdmin:password@p1213-master.p1213.cecc.ihost.com:31466")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
