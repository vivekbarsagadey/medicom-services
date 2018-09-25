
from com.medicom.health.diabetes.domain.patient_features import PatientFeatures
import csv
import json

csvfile = open('C:/Users/user/Desktop/user_diabetes.csv', 'r')
jsonfile = open('C:/Users/user/Desktop/user_data.json', 'w')

class PatientDataParser():

    def getPatientListFromFile(self, user=None, fileName=None):
        print("user",user)
        print("fileName", fileName)
        patientFeaturesList = []
        patientFeaturesList.append(PatientFeatures());
        reader = csv.DictReader(csvfile, patientFeaturesList)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

        return True