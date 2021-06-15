from pymongo import MongoClient
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
#Go to the database which is already created and prin the data
db = client["newdb"]
col = db["reviews"]
x = col.find()
for data in x:
    print(data)
