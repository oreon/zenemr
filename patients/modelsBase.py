
from django.db import models

    
CustomerType = (
    ('0', 'BRONZE'),
    ('1', 'SILVER'),
    ('2', 'GOLD'),
  
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
        
    
      
        

    
 

class DrugBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    price = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    image = models.ImageField(null = False, blank =  True, )
    
    categorys =    models.ManyToManyField("patients.Category",  blank=True,  related_name="categorys")
            
        
    
    displayTill = models.DateField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class CategoryBase(models.Model): 

    drugs =    models.ManyToManyField("patients.Drug",  blank=True,  related_name="drugs")
            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientBase(PersonBase): 

    customerType = models.CharField(null = False, blank =  True, max_length = 1 , choices = CustomerType)
    
            
        
    
            
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionBase(models.Model): 

            
        
    
    notes = models.TextField(null = False, blank =  True, )
    
    isCurrent = models.NullBooleanField(null = False, blank =  True, )
    
        
    encounter =    models.OneToOneField("patients.Encounter",  blank=True,  related_name="encounter")
        
    
    patient = models.ForeignKey('patients.Patient', related_name='prescription')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def encounterDisplayName(self):
        return self.encounter.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.notes 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionItemBase(models.Model): 

    prescription = models.ForeignKey('patients.Prescription', related_name='prescriptionItems')
        
    qty = models.PositiveIntegerField(null = False, blank =  True, )
    
    drug = models.ForeignKey('patients.Drug', related_name='prescriptionItem')
        
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    
    
    def __str__(self):
        return self.drug.displayName + "" 
        
    class Meta:
        abstract = True
        
    
      
        unique_together = ("prescription", "drug")
      
        


 

class EmployeeBase(PersonBase): 

    active = models.NullBooleanField(null = False, blank =  True, )
    
        
    #appUser =    models.OneToOneField("users.AppUser",  blank=True,  related_name="appUser")
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def appUserDisplayName(self):
        return self.appUser.__str__()
    
    
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
    
        
    prescription =    models.OneToOneField("patients.Prescription", null=True, blank=True,  related_name="prescription")
        
    
    patient = models.ForeignKey('patients.Patient', related_name='encounter')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
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
        
    
      
        

  