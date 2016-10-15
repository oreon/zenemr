
from django.db import models
from .modelsBase import *
    
class Patient(PatientBase): 
        pass
    

class Person(PersonBase): 
    class Meta:
        abstract = True
    

class Vaccination(VaccinationBase): 
        pass
    

class Encounter(EncounterBase): 
        pass
    

class Vaccine(VaccineBase): 
        pass
    

class LabTest(LabTestBase): 
        pass
    

class TestResults(TestResultsBase): 
        pass
    

class ResultRow(ResultRowBase): 
        pass
    

  