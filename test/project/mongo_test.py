import pymongo
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.packet_unsearched
a = [1, 2, 3, 4, 5]
collection_one = db.one
for i in a:
  collection_one.insert_one({'packet': i})

print(collection_one.size)
