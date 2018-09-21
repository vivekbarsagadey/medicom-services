
path = '../src/com/medicom/health/diabetes/store/'
#filename = path+'all_model.sav'
file_ext = '.sav'



import pickle
import sys
from pathlib import Path


class StoreHandle:
    def getModel(self, name="all_model"):
        config = Path(path+name+file_ext)
        return pickle.load(open(path+name+file_ext, 'rb'))

    def saveModel(self , name="all_model", model=None):
        pickle.dump(model, open(path+name+file_ext, 'wb'))
