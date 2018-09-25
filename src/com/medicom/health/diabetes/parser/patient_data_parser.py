
from com.medicom.health.diabetes.domain.patient_features import PatientFeatures

class PatientDataParser:

    def getPatientListFromFile(self, user=None, fileName=None):
        print("user",user)
        print("fileName", fileName)
        patientFeaturesList = []
        patientFeaturesList.append(PatientFeatures());
