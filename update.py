from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#Go to the database which is already created
db = client["newdb"]
col = db["reviews"]
#We are updating the name to " Spoon Delecious Company" for Vegetarian cuisine
oldval = { "cuisine": "Vegetarian" }
newvalues = { "$set": { "name": "Spoon Delecious Company" } }
#print before the update:
print("Before Update \n")
for x in col.find():
  print(x)
col.update_one(oldval, newvalues)
#print after the update:
print("\n After Update \n")
for x in col.find():
  print(x)
