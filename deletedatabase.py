from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#enter database name below in 'DATABASE-NAME' which you want to delete
client.drop_database('DATABASE-NAME')
print("Database deleted")
