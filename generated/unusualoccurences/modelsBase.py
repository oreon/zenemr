
from django.db import models

    
TreatmentCategory = (
    ('0', 'Radiation'),
    ('1', 'Chemotherapy'),
    ('2', 'Anesthesia'),
    ('3', 'Surgery'),
    ('4', 'Other'),
  
)

Severity = (
    ('0', 'Mild'),
    ('1', 'Moderate'),
    ('2', 'Critical'),
  
)

    
 

class UnusualOccurenceBase(models.Model): 

    occurenceType = models.ForeignKey('unusualoccurences.OccurenceType', related_name='unusualOccurence')
        
    
    category = models.CharField(null = False, blank =  True, max_length = 1 , choices = TreatmentCategory)
    
    severity = models.CharField(null = False, blank =  True, max_length = 1 , choices = Severity)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def occurenceTypeDisplayName(self):
        return self.occurenceType.__str__()
    
    
    def __str__(self):
        return self.description 
        
    class Meta:
        abstract = True
        
    
      
        


 

class OccurenceTypeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  