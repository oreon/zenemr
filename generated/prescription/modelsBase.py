
from django.db import models

    
Route = (
    ('0', 'PO'),
    ('1', 'IV'),
    ('2', 'IM'),
    ('3', 'SC'),
    ('4', 'TOPICAL'),
  
)

    
 

class PrescriptionTemplateBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    directivesForPatient = models.TextField(null = False, blank =  True, )
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionBase(models.Model): 

            
        
    
    active = models.NullBooleanField(null = False, blank =  True, )
    
    directivesForPatient = models.TextField(null = False, blank =  True, )
    
    drugs = models.CharField(null = False, blank =  True, max_length=30)
    
    startDate = models.DateField(null = False, blank =  True, )
    
    endDate = models.DateField(null = False, blank =  True, )
    
        
    encounter =    models.OneToOneField("patients.Encounter",  null =  False,blank=True,  related_name="encounter")
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def encounterDisplayName(self):
        return self.encounter.__str__()
    
    
    def __str__(self):
        return drugs 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionItemBase(models.Model): 

    drug = models.ForeignKey('drugs.Drug', related_name='prescriptionItem')
        
    
    qty = models.CharField(null = False, blank =  True, )
    
    strength = models.CharField(null = False, blank =  True, max_length=30)
    
    prescription = models.ForeignKey('prescription.Prescription', related_name='prescriptionItems')
        
    
    route = models.CharField(null = False, blank =  True, max_length = 1 , choices = Route)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    frequency = models.ForeignKey('prescription.Frequency', related_name='prescriptionItem')
        
    
    remarks = models.CharField(null = False, blank =  True, max_length=30)
    
    brandName = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def frequencyDisplayName(self):
        return self.frequency.__str__()
    
    
    def __str__(self):
        return self.strength 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionItemTemplateBase(models.Model): 

    drug = models.ForeignKey('drugs.Drug', related_name='prescriptionItemTemplate')
        
    
    qty = models.CharField(null = False, blank =  True, )
    
    frequency = models.ForeignKey('prescription.Frequency', related_name='prescriptionItemTemplate')
        
    
    strength = models.CharField(null = False, blank =  True, max_length=30)
    
    route = models.CharField(null = False, blank =  True, max_length = 1 , choices = Route)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    remarks = models.CharField(null = False, blank =  True, max_length=30)
    
    brandName = models.CharField(null = False, blank =  True, max_length=30)
    
    prescriptionTemplate = models.ForeignKey('prescription.PrescriptionTemplate', related_name='prescriptionItemTemplates')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def frequencyDisplayName(self):
        return self.frequency.__str__()
    @property   
    def prescriptionTemplateDisplayName(self):
        return self.prescriptionTemplate.__str__()
    
    
    def __str__(self):
        return self.strength 
        
    class Meta:
        abstract = True
        
    
      
        


 

class FrequencyBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    qtyPerDay = models.PositiveIntegerField(null = False, blank =  True, )
    
    remarkts = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  