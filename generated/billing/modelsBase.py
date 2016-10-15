
from django.db import models


    
 

class InvoiceBase(models.Model): 

            
        
    
    notes = models.CharField(null = False, blank =  True, max_length=30)
    
    totalAmount = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    paidAmount = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    patient = models.ForeignKey('patients.Patient', related_name='invoice')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.notes 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ServiceBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    price = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class InvoiceItemBase(models.Model): 

    units = models.PositiveIntegerField(null = False, blank =  True, )
    
    service = models.ForeignKey('billing.Service', related_name='invoiceItem')
        
    
    invoice = models.ForeignKey('billing.Invoice', related_name='invoiceItems')
        
    
    appliedPrice = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    total = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def serviceDisplayName(self):
        return self.service.__str__()
    @property   
    def invoiceDisplayName(self):
        return self.invoice.__str__()
    
    
    def __str__(self):
        return self.units+ "" 
        
    class Meta:
        abstract = True
        
    
      
        

  