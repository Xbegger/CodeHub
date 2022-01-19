

import sys
from base64 import b64decode, b64encode
from threading import Event, Thread
import zlib
from pymongo import MongoClient
from scapy import fields

if sys.version_info >= (3,):
    from queue import Queue
    import _pickle as cPickle
else:
    import cPickle
    from Queue import Queue

def synced(func):
    '''
    Decorator for functions that should be called synchronously from another thread
    
    :param func: function to call
    '''
    def wrapper(self, *arg, **kwargs):
        '''
        inner wrapper for the synchronous function
        '''
        task = DataManager(func, *arg, **kwargs)
        self.submit_task(task)
        return task.get_results()
    return wrapper

class DataManager(Thread):

    def __init__(self, dbname):
        super(DataManager, self).__init__()
        self._queue = Queue()
        self._dbname = dbname
        self._connection = None
        self._cursor = None
        self._session_info = None
        self._reports = None
        
        self._stopped_event = Event()
        self._vaolatile_data = {}

        self._DST_STRING = "127.0.0.1:27017"

    def run(self):
        '''
        thread function
        '''
        self._stopped_event.clear()
        self.open()
        while True:
            task = self._queue.get()
            if task is None:
                break
            task.execute(self)
        self.close()
        self._stopped_event.set()



    def submit_task(self, task):
        '''
        submit a task to the data manager, tobe proccessed in the DataManager context
        
        :type task: DataManagerTask
        :param task: task to perform
        '''
        self._queue.put(task)
        return task


    def open(self):
        '''
        open the database
        '''
        self._client = MongoClient(self.DST_STRING)
        self._connection = self._client[self._dbname]
        self._cursor
        self._session_info = SessionInfoCollection(self._connection)
        self.reports = ReportsCollection(self._connection)


    def close(self):
        '''
        close the database connection
        '''
        self._client.close()
    
    def stop(self):
        '''
        Stop the data manager
        '''
        self.submit_task(None)
        self._stopped_event.wait()

    
    @synced
    def get_session_info_manager(self):
        return self._session_info
    

    @synced
    def get_session_info(self):
        return self._session_info.get_session_info()
    
    @synced
    def set_session_info(self, info):
        self._session_info.set_session_info(info)
    
    @synced
    def get_reports_manager(self):
        return self._reports
    
    @synced
    def get_report_test_ids(self):
        return self._reports.get_report_test_ids()

    @synced
    def get_report_list(self):
        return self._reports.get_report_list()

    @synced
    def get_report_by_id(self, report_id):
        return self._reports.get(report_id)
    
    @synced
    def store_report(self, report, test_id):
        self._reports.store(report, test_id)

    @synced
    def set(self, key, data):
        if isinstance(data, dict):
            self._volatile_data[key] = {k:v for (k, v) in data.items()}
        else:
            self._volatile_Data[key] = data
    
    @synced
    def get(self, key):
        return self._volatile_data.get(key, None)

class Collection(object):
    '''
    Base class for data manager collection
    '''
    __COLLECTION_FIELDS__ = []
    __COLLECTION_NAME__ = None

    def __init__(self, connection):
        '''

        '''
        self._connection = connection

        self._name = type(self).__COLLECTION_NAME__
        self._fields = type(self).__COLLECTION_FIELDS__
        self._create_collection()
    

    def _create_collection(self):
        '''
        create the current collection if nnot exists
        '''
        self._connection[self._name]

    
    def select(self, to_select, where=None):
        '''
        select db entries
        :param to_select:the formate of the query
        :param where:the condition of the query, which items need to be returned
        '''
        if to_select != None:
            res_fields = { field:1 for field in to_select}
        else:
            res_fields = {}
        
        if where == None:
            where = {}
        self._cursor = self._connection[self._name].find(where, res_fields)
        res = list(self._cursor.clone())
        return res




    # def row_to_dict(self, row):
    #     res = {}
    #     for i in range(len(self._fields)):
    #         res[self._fields[i][0]] = row[i]
    #         return res
    
    def update(self, field_dict, where_clause=None):
        '''
        update db entry

        :param field_dict:dictionary of fields and values
        :param where_clause: where clause for the update
        '''
        self._connection[self._name].update_one(where_clause, {"$set":field_dict})



    def insert(self, field_value_dict):
        '''
        insert new db entry
        :param field_value_dict: dict of fields-values pair to insert
        '''
        return self._connection[self._name].insert_one(field_value_dict)


class ReportsCollection(Collection):
    '''
    Collection for storing the reports
    '''
    __COLLECTION_NAME__ = 'conf'
    __COLLECTION_FIELDS__ = [
        ('_id', 'INTEGER PRIMARY KEY'),
        ('test_id', '64-bit integer'),
        ('content', 'String'),
        ('status', 'String'),
        ('reason', 'String'),
        ('protocol','String'),
        ('plc_type', 'String'),
        ('duration', 'Double'),
        ('create_time', 'Date')
    ]

    def __init__(self, connection):
        super(ReportsCollection, self).__init__(connection)
    
    def store(self, report, test_id):
        report_d = report.to_dict()
        content = self._serialize_dict(report_d)
        report_id = self.insert({
            'test_id': test_id,
            'content':content,
            'status':report.get_status(),
            'reason':report.get('reason'),
            'protocol':report.get('prootocol'),
            'plc_type':report.get('plc_type'),
            'duration':report.get('duration'),
            'create_time':report.get('create_time'),
        })['insertedId']
        return report_id

    
    def get(self, test_id):
        '''
        get report by the test id

        :param test_id: test id
        :return: Report object
        '''
        self.select(None, {'test_id':test_id})
        row = self._cursor.next()
        if not row:
            raise KeyError("No report with test id %s in the DB" % test_id)
        
        content = self._deserialize_dict(row['content'])
        return Report.from_dict(content)

    def get_report_test_ids(self):
        '''
        :return: ids of test reports
        '''
        self.select(None)
        res = []
        for row in self._cursor:
            # print(row)
            res.append(row['_id'])
        return res
    
    def get_report_list(self):
        self.select(['test_id', 'status', 'reason'])
        res = list(self._cursor)
        return res

    @classmethod
    def _serialize_dict(cls, data):
        '''
        serializes a  dictionary
        '''
        return b64encode(zlib.compress(cPickle.dumps(data, protocol=2))).decode()

    @classmethod
    def _deserialize_dict(cls, data):
        '''
        deserializes a dictionary
        '''
        return cPickle.loads(zlib.decompress(b64decode(data.encode())))


class SessionInfoCollection(Collection):
    '''
    Collection for storing the session info
    '''
    __COLLECTION_NAME__ = "info"
    __COLLECTION_FIELDS__ = [
        ('start_time', 'INT'),
        ('start_index', 'INT'),
        ('end_index', 'INT'),
        ('current_index', 'INT'),
        ('failure_count', 'INT'),
        ('kitty_version', 'BLOB'),
        ('data_model_hash', 'INT'),
        ('test_list_str', 'BLOB')
    ]
    
    def __init__(self, connection):
        '''
        '''
        super(SessionInfoCollection, self).__init__(connection)
        self.info = self.read_info()

    def read_info(self):
        self.select(None)
        info_d = self._cursor.next()
        if not info_d:
            return None
        return SessionInfo.from_dict(info_d)

    def set_session_info(self, info):
        '''
        
        '''
        if not self.info:
            self.info = SessionInfo()
            info_d = self.info.as_dict()
            self.insert(info_d)
        changed = self.info.copy(info)
        if changed:
            self.update(self.info.as_dict())
        
    def get_session_info(self):
        if self.info:
            return SessionInfo(self.info)
        return None

class SessionInfo(object):
    '''
    session information manager
    '''

    fields = [i[0] for i in SessionInfoCollection.__COLLECTION_FIELDS__]

    def __init__(self, orig=None):
        '''
        :param orig: SessionInfo object to copy
        '''
        self.start_time = 0
        self.start_index= 0
        self.current_index = 0
        self.end_index = None
        self.failure_count = 0
        self.kitty_version = ''
        self.data_model_hash = 0
        self.test_list_str = ''
        if orig:
            self.copy(orig)

    def copy(self, orig):
        '''
        :param orig: ASessionInfo object to copy
        :return: True if changed, false otherwise
        '''
        changed = False
        for attr in SessionInfo.fields:
            oattr = getattr(orig, attr)
            if getattr(self, attr) != oattr:
                setattr(self, attr, oattr)
                changed = True
        return changed

    def as_dict(self):
        '''
        :return: dictionary with the object fields
        '''
        return {fname: getattr(self, fname) for fname in SessionInfo.fields}

    @classmethod
    def from_dict(cls, info_d):
        '''
        :param: info_d: the info dictionary
        :rtype: SessionInfo
        :return: object that corresponds to the info dictionary
        '''
        info = SessionInfo()
        for k, v in info_d.items():
            setattr(info, k, v)
        return info





client = MongoClient("127.0.0.1:27017")
connection = client["base"]
# # cursor = connection["conf"].find({},{})

# report = ReportsCollection(connection)

# print(report.get_report_test_ids())



cursor = connection['info'].find()
info = SessionInfoCollection(connection)

# info.insert(SessionInfo().as_dict())
print(info.get_session_info().start_time)