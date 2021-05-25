from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#Go to the database which is already created
db = client["newdatabase"]
col = db["newcollection"]
oldval = { "name": "Jas", "address": "Highway 37", "State": "Karnataka", "Country": "India" }
newvalues = { "$set": { "address": "Canyon 123" } }
#print before the update:
for x in col.find():
  print(x)
col.update_one(oldval, newvalues)
#print after the update:
for x in col.find():
  print(x)
