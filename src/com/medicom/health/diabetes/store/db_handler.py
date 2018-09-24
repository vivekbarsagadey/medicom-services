from pymongo import MongoClient
class DBHandler:
    def __init__(self):
        print("DBHandler init")
    def connect_db(self):
        global db
        connection = MongoClient()
        dbs = connection.the_platfrom_db
        db = dbs.userString
        return (db)
    def getDataSource(self):

        return (db)

    def getUserDataSource(self):
        return db.user