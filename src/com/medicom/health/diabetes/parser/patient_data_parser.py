import csv
import re

from com.medicom.health.diabetes.parser.patient_features import PatientFeatures

csvfile = open('C:/Users/user/Desktop/user_diabetes.csv', 'r')
fieldname = ('patientId','pregnancy','glucose','bloodpressure','skinThickness','insulin','bmi','diabetesPedigreeFunction','age')
word_regex_pattern = re.compile("[^A-Za-z]+")

def camel(chars):
  words = word_regex_pattern.split(chars)
  return "".join(w.lower() if i is 0 else w.title() for i, w in enumerate(words))

class PatientDataParser():
    def __init__(self):
        print("the parser method is called.")

    def getPatientListFromFile(self):
        print("patient features loaded")
        reader = csv.DictReader(csvfile,fieldname)
        for row in reader:
            #print("new row",row)
            print("Storing the Features in Database")
            patientFeatures = PatientFeatures(org=row)
            #print("age >>> ",patientFeatures.age)
            patientFeatures.save();
            print("Features saved to database sucessfully.")

        return True