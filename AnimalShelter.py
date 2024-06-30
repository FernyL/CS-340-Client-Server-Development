# CRUD Python Module
import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'Fern1234'
        USER = urllib.parse.quote_plus(username)
        PASS = urllib.parse.quote_plus(password)
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32713
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        #self.client = MongoClient('mongodb://%s:%s@localhost:32713/?authMechanism=DEFAULT&authSource=AAC' % (username,password))
        #self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data) # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, queryData):
        if queryData:
            data = self.database.animals.find(queryData, {"_id":False})
        else:
            data = self.database.animals.find({}, {"_id":False})
        return data
    
# Create method to implement the U in CRUD.
    def update(self, queryData, updateData):
        if queryData is not None and updateData is not None:
            newData = self.database.animals.update_many(queryData, { "$set": updateData}) 
        else:
            return "{}"
        return newData

# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            removedData = self.database.animals.delete_one(deleteData)
        else:
            return "{}"
        return removedData
            
