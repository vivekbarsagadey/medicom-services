import pandas as pd
import json
from com.medicom.health.diabetes.store.db_handler import DBHandler
from pymongo import MongoClient

class User:
    def __init__(self ,org={}):
        self.firstName = org['firstName']
        self.lastName = org['lastName']
        self.pregnancy = org['pregnancy']
        self.glucose = org['glucose']
        self.bloodpressure = org['bloodpressure']
        self.skinThickness = org['skinThickness']
        self.insulin = org['insulin']
        self.bmi = org['bmi']
        self.diabetesPedigreeFunction = org['diabetesPedigreeFunction']
        self.age = org['age']
        self.outcome=0

    def __str__(self):
        return str(self.__dict__)

    def save(self):

        user_val = json.dumps(self.__dict__)
        print("User json is ")
        print(user_val)
        #DBHandler().connect_db()
        connection = MongoClient('localhost', 27017)
        dbs = connection.the_platfrom_db
        '''DBHandler().connect_db()
        data = json.loads(user_String().read())

        for item in data:
            db.insert(item)'''


        dbs.userString.insert(user_val)
    def getFrame(self ):

        return pd.DataFrame(
            {'Pregnancies': self.pregnancy, 'Glucose': self.glucose, 'BloodPressure': self.bloodpressure, 'SkinThickness': self.skinThickness,
             'Insulin': self.insulin, 'BMI': self.bmi,
             'DiabetesPedigreeFunction': self.diabetesPedigreeFunction, 'Age': self.age}, index=[0])

