import pymongo
from pymongo import MongoClient
from random import randint
#Step 1: Connect to MongoDB
client = MongoClient("mongodb://Username:password@HOSTNAME:NODEPORT")
db=client.newdb
#Step 2: Create sample data
names = ['Spoon','Tree','Country', 'Delecious', 'Large','City','Pond', 'Mozzarella','Elephant', 'Salty','Burger','Energetic', 'Funny']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Indian', 'Indonesian', 'Italian', 'Mexican', 'American', 'Japanese', 'Vegetarian']
for x in range(1, 100):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 100 business reviews')
