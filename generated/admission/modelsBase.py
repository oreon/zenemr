
from django.db import models

    
DischargeCode = (
    ('0', 'Deceased'),
    ('1', 'Referred'),
    ('2', 'Normal'),
  
)

    
 

class AdmissionBase(models.Model): 

    admissionNote = models.TextField(null = False, blank =  True, )
    
    dischargeDate = models.DateField(null = False, blank =  True, )
    
    dischargeNote = models.TextField(null = False, blank =  True, )
    
    dischargeCode = models.CharField(null = False, blank =  True, max_length = 1 , choices = DischargeCode)
    
    currentBed = models.CharField(null = False, blank =  True, max_length=30)
    
    isCurrent = models.NullBooleanField(null = False, blank =  True, )
    
    invoice = models.ForeignKey('billing.Invoice', related_name='admission')
        
    
            
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def invoiceDisplayName(self):
        return self.invoice.__str__()
    
    
    def __str__(self):
        return self.admissionNote 
        
    class Meta:
        abstract = True
        
    
      
        


 

class BedStayBase(models.Model): 

    fromDate = models.DateField(null = False, blank =  True, )
    
    toDate = models.DateField(null = False, blank =  True, )
    
    admission = models.ForeignKey('admission.Admission', related_name='bedStays')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def admissionDisplayName(self):
        return self.admission.__str__()
    
    
    def __str__(self):
        return self.fromDate+ "" 
        
    class Meta:
        abstract = True
        
    
      
        

  