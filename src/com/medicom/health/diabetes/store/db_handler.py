import pymongo
from pymongo import MongoClient

connection = MongoClient()
dbs = connection.the_platfrom_db
db = dbs.userString
class DBHandler:
    def __init__(self):
        print("DBHandler init")
        print(connection.list_database_names())
    def getDataSource(self):
       return (db)

    def getUserDataSource(self):
        return db.user