# formatPatientInfo: Formats patient information (attributes) in the same format used in the “patients.txt” file (i.e., has underscores between values)✅
# __str__: Formats patient information - for display, see Sample Run, “Display Patient’s List”✅


# enterPatientInfo: Asks the user to enter patient information (attributes), then creates and returns a new Patient object✅
# readPatientsFile: Reads “patients.txt” file into a list of Patient objects✅
# searchPatientById: Searches the list of Patient objects for a specified patient ID using the patient ID that the user enters. Returns Patient object or -1 if not found.✅
# editPatientInfo: Finds patient ID in the list of Patient objects, prompts for new values and updates the remaining attributes✅
# displayPatientsList: Displays all the Patients’ information(attributes) in patients list✅
# writePatientListToFile: Writes “patients.txt” file from the list of Patient objects, maintaining correct formatting✅
# addPatientToList: Gets new Patient object (with user-entered patient information) and adds it to the patients list✅
patients = []
# patients class

readPatientsFile("patients.txt")


class Patients(object):
    # patient attributes
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    # txt file for patient attributes
    def readPatientsFile(patients):
        with open('./txt/patients.txt') as patients:
            attributes = patients.read()
            for patientAttribute in attributes:
                displayPatientsList = attributes.replace('_', ' ')
        patients.close()
        print(displayPatientsList)

    # formats patient information (!!!!!!SAME FORMAT AS TXT FILE!!!!!!!)
    def formatPatientInfo(self):
        return format(self.id, self.name, self.diagnosis, self.gender, self.age)

    # prints patient information
    def __str__(self):
        patientAttribute = self.formatPatientInfo()
        return patientAttribute

    # Asks the user to enter patient information
    def enterPatientInfo():
        with open('patients.txt', mode='w') as patients:
            newID = patients.write(input('Enter Patient ID: '))
            newName = patients.write(input('Enter Patient Name: '))
            newDiagnosis = patients.write(input('Enter Patient diagnosis: '))
            newGender = patients.write(input('Enter Patient gender: '))
            newAge = patients.write(input('Enter Patient age: '))
            newPatient = Patients(
                newID, newName, newDiagnosis, newGender, newAge)
            return newPatient

    # search for specific patient information
    def searchPatientById(id):
        for patient in patients:
            if patient.id == id:
                return patient

    # edit patient information
    def editPatientInfo(id):
        for patient in patients:
            patients.id = input('Enter new patient id: ')
            patients.name = input('Enter new patient name: ')
            patients.diagnosis = input('Enter new patient diagnosis: ')
            patients.gender = input('Enter new patient gender: ')
            patients.age = input('Enter new patient age: ')

    def writePatientsListToFile(patients):
        with open('./txt/patients', mode='w') as file:
            for patient in patients:
                file.write('\n', patient)

    # adds to patient list
    def addPatientToList():
        newPatient = enterPatientInfo()
        patients.append(newPatient)
