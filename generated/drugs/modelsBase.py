
from django.db import models

    
InteractionSeverity = (
    ('0', 'MILD'),
    ('1', 'MODERATE'),
    ('2', 'SEVERE'),
  
)

    
 

class AtcDrugBase(models.Model): 

    code = models.CharField(null = False, blank =  True, max_length=30)
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
    drug = models.ForeignKey('drugs.Drug', related_name='atcDrug')
        
    
    parent = models.ForeignKey('drugs.AtcDrug', related_name='subcategories')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def parentDisplayName(self):
        return self.parent.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    absorption = models.TextField(null = False, blank =  True, )
    
    biotransformation = models.TextField(null = False, blank =  True, )
    
    atcCodes = models.CharField(null = False, blank =  True, max_length=30)
    
    contraIndication = models.TextField(null = False, blank =  True, )
    
    description = models.TextField(null = False, blank =  True, )
    
    dosageForm = models.CharField(null = False, blank =  True, max_length=30)
    
    foodInteractions = models.TextField(null = False, blank =  True, )
    
    halfLife = models.TextField(null = False, blank =  True, )
    
    indication = models.TextField(null = False, blank =  True, )
    
    halfLifeNumberOfHours = models.CharField(null = False, blank =  True, )
    
    mechanismOfAction = models.TextField(null = False, blank =  True, )
    
    patientInfo = models.TextField(null = False, blank =  True, )
    
    pharmacology = models.TextField(null = False, blank =  True, )
    
            
        
    
    drugCategorys =    models.ManyToManyField("drugs.DrugCategory",  blank=True,   null = True,  related_name="drugCategorys")
            
        
    
    toxicity = models.TextField(null = False, blank =  True, )
    
    routeOfElimination = models.TextField(null = False, blank =  True, )
    
    volumeOfDistribution = models.CharField(null = False, blank =  True, max_length=30)
    
    drugBankId = models.CharField(null = False, blank =  True, max_length=30)
    
    categories = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugInteractionBase(models.Model): 

    description = models.TextField(null = False, blank =  True, )
    
    drug = models.ForeignKey('drugs.Drug', related_name='drugInteractions')
        
    
    interactingDrug = models.ForeignKey('drugs.Drug', related_name='drugInteraction')
        
    
    severity = models.CharField(null = False, blank =  True, max_length = 1 , choices = InteractionSeverity)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def interactingDrugDisplayName(self):
        return self.interactingDrug.__str__()
    
    
    def __str__(self):
        return self.description 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    drugs =    models.ManyToManyField("drugs.Drug",  blank=True,   null = True,  related_name="drugs")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  