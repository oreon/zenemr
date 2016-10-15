
from django.db import models


    
 

class OrderTemplateBase(models.Model): 

 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.Empty class - no display name possible 
        
    class Meta:
        abstract = True
        
    
      
        


 

class OrderBase(models.Model): 

    orderTemplate = models.ForeignKey('physicianOrder.OrderTemplate', related_name='order')
        
    
    patient = models.ForeignKey('patients.Patient', related_name='order')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def orderTemplateDisplayName(self):
        return self.orderTemplate.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.orderTemplate+ "" 
        
    class Meta:
        abstract = True
        
    
      
        

  