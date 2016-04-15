
# imports
# import unicode
import os
import io
import json
import pymongo
from pprint import pprint as pp
import csv
from collections import namedtuple
import time
from pymongo import MongoClient as MCLi

class IO_csv(object):
    def __init__(self, filepath, filename, filesuffix='csv'):
        self.filepath = filepath       # /path/to/file  without the '/' at the end
        self.filename = filename       # FILE_NAME
        self.filesuffix = filesuffix
        # self.file_io = os.path.join(dir_name, '.'.join((base_filename, filename_suffix)))

    def save(self, data, NTname, fields):
        # NTname = Name of the NamedTuple
        # fields = header of CSV - list of the fields name
        NTuple = namedtuple(NTname, fields)
        
        if os.path.isfile('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix)):
            # Append existing file
            with open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), 'ab') as f:
                writer = csv.writer(f)
                # writer.writerow(fields) # fields = header of CSV
                writer.writerows([row for row in map(NTuple._make, data)])
                # list comprehension using map on the NamedTuple._make() iterable and the data file to be saved
                # Notice writer.writerows and not writer.writerow (i.e. list of multiple rows sent to csv file
        else:
            # Create new file
            with open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(fields) # fields = header of CSV - list of the fields name
                writer.writerows([row for row in map(NTuple._make, data)])
                #  list comprehension using map on the NamedTuple._make() iterable and the data file to be saved
                # Notice writer.writerows and not writer.writerow (i.e. list of multiple rows sent to csv file
            
    def load(self, NTname, fields):
        # NTname = Name of the NamedTuple
        # fields = header of CSV - list of the fields name
        NTuple = namedtuple(NTname, fields)
        with open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix),'rU') as f:
            reader = csv.reader(f)
            for row in map(NTuple._make, reader):
                # Using map on the NamedTuple._make() iterable and the reader file to be loaded
                yield row


class IO_json(object):
    def __init__(self, filepath, filename, filesuffix='json'):
        self.filepath = filepath        # /path/to/file  without the '/' at the end
        self.filename = filename        # FILE_NAME
        self.filesuffix = filesuffix
        # self.file_io = os.path.join(dir_name, '.'.join((base_filename, filename_suffix)))

    def save(self, data):
        if os.path.isfile('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix)):
            # Append existing file
            with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), 'a', encoding='utf-8') as f:
                f.write(unicode(json.dumps(data, ensure_ascii= False))) # In python 3, there is no "unicode" function 
                # f.write(json.dumps(data, ensure_ascii= False)) # create a \" escape char for " in the saved file        
        else:
            # Create new file
            with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), 'w', encoding='utf-8') as f:
                f.write(unicode(json.dumps(data, ensure_ascii= False)))
                # f.write(json.dumps(data, ensure_ascii= False))    

    def load(self):
        with io.open('{0}/{1}.{2}'.format(self.filepath, self.filename, self.filesuffix), encoding='utf-8') as f:
            return f.read()

class IO_mongo(object):
    conn={'host':'localhost','ip':'27017'}

    def __init__(self, db='twtr_db', coll='twtr_coll', **conn):
        self.client=MCLi(**conn)
        self.db=self.client[db]
        self.coll=self.db[coll]

    def save(self,data):
        return self.coll.insert(data)

    def load(self, return_cursor=False,criteria=None,projection=None):
        if criteria is None:
            criteria={}

        if Projection is None:
            cursor=self.coll.find(criteria)
        else:
            cursor=self.coll.find(criteria,projection)

        if return_cursor:
            return cursor
        else:
            return [iterm for item in cursor]
