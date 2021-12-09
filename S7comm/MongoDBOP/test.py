from winreg import DisableReflectionKey
from pymongo import MongoClient, collection

class MongoDBError(Exception):
    pass

class DataBaseMongoError(MongoDBError):
    pass


class t:
    def __init__(self) -> None:
        self.name = "test"



def get_databases():
    
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
# CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    
    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    dbList = client.list_database_names()

    return dbList, client


def create_database(name):
    dbList, client = get_databases()

    if name in dbList:
        raise DataBaseMongoError("DataBase is already created while create_datebase")
    return client[name]

def get_database(name):
    dbList, client = get_databases()
    if name in dbList:
        return client[name]
    return None

def get_collections(db):
    collectionList = db.list_collection_names()
    return collectionList

def get_collection(db, name):
    collectionList = get_collections(db)
    if name in collectionList:
        return db[name]
    return None

def create_collection(db, name):
    collectionList = get_collections(db)
    if name in collectionList:
        raise DataBaseMongoError("Collection is already created while create_collection")
    return db[name]

def insert(collection, items):

    if( len(items) == 1):
        res = collection.insert_one(items[0])
    else:
        res = collection.insert_many(items)
    return res



print(get_databases())
# testDB = create_database("test")
testDB = get_database("test")
print(get_databases())

post = {
    "int" : 2,
    "char" : 'c',
    "String" : "string1",
    "double" : 3.14,
    "boolean" : False,
    # "object" : t(),
    "list" : [1,2,3],
    "dict" : {"1":1, "2": 2}
}

print(get_collections(testDB))
# c = create_collection(testDB, "testCollection")
c = get_collection(testDB, "testCollection")
# print(insert(c, [post]))
for x in c.find_one({}, {"int":1, "char":1}):
    print(x)
