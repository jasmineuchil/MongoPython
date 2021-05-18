from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://myUserAdmin:password@HOSTNAME:NODEPORT")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
