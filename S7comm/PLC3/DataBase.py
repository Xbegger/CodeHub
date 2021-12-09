import re
from pymongo import MongoClient

class MongoDBError(Exception):
    pass

class DataBaseError(MongoDBError):
    pass

class CollectionError(MongoDBError):
    pass


class DataBase():

    def __init__(self) -> None:
        self.db = None
        self.client = None
        self.DST_STRING = ""
        self.collection = None
    
    def connect(self):
        self.client = MongoClient(self.DST_STRING)

    def setDST_STRING(self, s):
        self.DST_STRING = s

        
    # 获取数据库
    def get_dataBases(self):
        return self.client.list_database_names()

    def get_dataBase(self, dbName):
        if dbName in self.get_dataBases():
            return self.client[dbName]
        return None
    
    # 设置当前操作的数据库对象
    def set_dataBase(self, name):
        db = self.get_dataBase(name)
        self.db = db
    
    # 获取数据库集合
    def get_collections(self):
        return self.db.list_collection_names()
    
    def get_collection(self, collection_name):
        if collection_name in self.db.list_collection_names():
            return self.db[collection_name]
        return None

    def set_collection(self, collection_name):
        collection = self.get_collection(collection_name)
        self.collection = collection

    # CURD
    ## 插入文档
    '''
    @function：向指定的集合中插入文档
    @param collection：数据库的集合
    @param items：要插入的文档列表
    '''
    def insert(collection, items):
        if(collection == None):
            raise CollectionError("The collection is None while insert")
        if(len(items) == 1):
            result = collection.insert_one(items)
        else:
            result = collection.insert_many(items)

        return result

    ## 查询文档
    '''
    @function：从指定的集合中查询与query 字段值相同的一个文档
    @param collection:
    @param query: dict 查询文档的条件
    '''
    def find_one(collection, query):
        return collection.find_one(query)

    '''
    @function：从指定大的集合中查询与 query 字段值相同的所有文档，返回 show中字段为设置为 1 的字段
    @param query:
    @param show:决定在返回文档的哪些字段
    '''
    def find(collection, query, show):
        return collection.find(query, show)
    

    ## 删除文档


    def delete_one(collection, query):
        return collection.delete_one(query)
    

    def delete(collection, query):
        return collection.delete_many(query)



    ## 修改文档

    def update_one(collection, query, newValues):
        return collection.update_one(query, newValues)

    def update(collection, query, newValues):
        return collection.update_many(query, newValues)
    
    