import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs, json

from com.medicom.health.diabetes.domain.computation import Computation
from com.medicom.health.diabetes.services.data_handler import DiabetesDataSet





from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

models = []

models.append(('KNN', KNeighborsClassifier()))
models.append(('SVC', SVC()))
models.append(('LR', LogisticRegression()))
models.append(('DT', DecisionTreeClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('RF', RandomForestClassifier()))
models.append(('GB', GradientBoostingClassifier()))

class AllModels():
    def __init__(self):
        self.dataDataSet = DiabetesDataSet()
        self.data = self.dataDataSet.getDataSet()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.dataDataSet.getX(), self.dataDataSet.getY(),
                                                            stratify=self.data.Outcome, random_state=0)
        self.train()

    def train(self):
        names = []
        scores = []
        for name, model in models:
            model.fit(self.X_train, self.y_train)


    def predict(self):
        #print(json.dumps({'columns' : diabetes.columns} , cls=NumpyEncoder))
        names = []
        scores = []
        computationList = []
        for name, model in models:
            self.y_pred = model.predict(self.X_test)
            scores.append(accuracy_score(self.y_test, self.y_pred))
            names.append(name)
            computationList.append(Computation(name,accuracy_score(self.y_test, self.y_pred)).__dict__)

        #tr_split = pd.DataFrame({'Name': names, 'Score': scores})
        #print(tr_split)
        #print(tr_split.values)
        return computationList
        #return tr_split.to_json(orient='split')
