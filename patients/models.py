
from django.db import models
from .modelsBase import *
    
class Drug(DrugBase): 
        pass
    

class Category(CategoryBase): 
        pass
    

class Patient(PatientBase): 
        pass
    

class Prescription(PrescriptionBase): 
        pass
    

class PrescriptionItem(PrescriptionItemBase): 
        pass
    

class Person(PersonBase): 
    class Meta:
        abstract = True
    

class Employee(EmployeeBase): 
        pass
    

class Vaccination(VaccinationBase): 
        pass
    

class Encounter(EncounterBase): 
        pass
    

class Vaccine(VaccineBase): 
        pass
    

  