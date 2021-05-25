from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#create new database
db = client["newdatabase"]
col = db["newcollection"]
#Create sample data
mydict = { "name": "Jas", "address": "Highway 37", "State": "Karnataka", "Country": "India" }
x = col.insert_one(mydict)
print("Database created successfully")
