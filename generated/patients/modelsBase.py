
from django.db import models

    
EmployeeType = (
    ('0', 'BRONZE'),
    ('1', 'SILVER'),
    ('2', 'GOLD'),
  
)

Title = (
    ('0', 'Mr'),
    ('1', 'Mrs'),
    ('2', 'Ms'),
    ('3', 'Dr'),
  
)

AllergySeverity = (
    ('0', 'SEVERE'),
    ('1', 'MODERATE'),
    ('2', 'MILD'),
  
)

Route = (
    ('0', 'PO'),
    ('1', 'IV'),
    ('2', 'IM'),
    ('3', 'SC'),
    ('4', 'TOPICAL'),
  
)

Gender = (
    ('0', 'F'),
    ('1', 'M'),
  
)

    
  

class PersonBase(models.Model): 

    firstName = models.CharField(null = False, blank =  False, max_length=30)
    
    lastName = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return ''.join([self.firstName , ', ', self.lastName]) 
        
    class Meta:
        abstract = True
        
    
      
        

    
 

class PatientBase(PersonBase): 

    customerType = models.CharField(null = False, blank =  True, max_length = 1 , choices = EmployeeType)
    
            
        
    
            
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class VaccinationBase(models.Model): 

    review = models.TextField(null = False, blank =  True, )
    
    rating = models.PositiveIntegerField(null = False, blank =  True, )
    
    vaccine = models.ForeignKey('patients.Vaccine', related_name='vaccination')
        
    
    patient = models.ForeignKey('patients.Patient', related_name='vaccination')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def vaccineDisplayName(self):
        return self.vaccine.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.review 
        
    class Meta:
        abstract = True
        
    
      
        


 

class EncounterBase(models.Model): 

    reason = models.TextField(null = False, blank =  True, )
    
    patient = models.ForeignKey('patients.Patient', related_name='encounter')
        
    
    labTests =    models.ManyToManyField("patients.LabTest",  blank=True,   null = True,  related_name="labTests")
            
        
    
        
    prescription =    models.OneToOneField("prescription.Prescription",  null = True,blank=True,  related_name="prescription")
        
    
    admission = models.ForeignKey('admission.Admission', related_name='encounter')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def admissionDisplayName(self):
        return self.admission.__str__()
    
    
    def __str__(self):
        return self.reason 
        
    class Meta:
        abstract = True
        
    
      
        


 

class VaccineBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class LabTestBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    encounters =    models.ManyToManyField("patients.Encounter",  blank=True,   null = True,  related_name="encounters")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class TestResultsBase(models.Model): 

    patient = models.ForeignKey('patients.Patient', related_name='testResults')
        
    
            
        
    
    labTest = models.ForeignKey('patients.LabTest', related_name='testResults')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def labTestDisplayName(self):
        return self.labTest.__str__()
    
    
    def __str__(self):
        return self.patient+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ResultRowBase(models.Model): 

    testResults = models.ForeignKey('patients.TestResults', related_name='resultRows')
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    value = models.CharField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def testResultsDisplayName(self):
        return self.testResults.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  