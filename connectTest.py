import pymongo
from pprint import pprint

# Connect to Atlas cluster
#client = pymongo.MongoClient("mongodb+srv://analytics:analytics-password@cluster0.fcrdz.mongodb.net/test?retryWrites=true&w=majority")
# Connect to local database
client = pymongo.MongoClient("localhost",27017)
db = client.sample_airbnb
collection = db.listingsAndReviews

# Query
cursor = collection.find({"bed_type":"Real Bed"})
print(cursor.count())
#for document in cursor:
#    pprint(document)