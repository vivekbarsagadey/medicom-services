import pandas as pd
import json
from com.medicom.health.diabetes.store.db_handler import DBHandler


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

        user_String = json.dumps(self.__dict__)
        print("User json is ")
        print(user_String)
        DBHandler().getDataSource().insert_one(user_String)

    def getFrame(self ):

        return pd.DataFrame(
            {'Pregnancies': self.pregnancy, 'Glucose': self.glucose, 'BloodPressure': self.bloodpressure, 'SkinThickness': self.skinThickness,
             'Insulin': self.insulin, 'BMI': self.bmi,
             'DiabetesPedigreeFunction': self.diabetesPedigreeFunction, 'Age': self.age}, index=[0])

