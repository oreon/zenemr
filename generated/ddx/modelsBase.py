
from django.db import models

    
LabFindingType = (
    ('0', 'ELEVATED'),
    ('1', 'DECREASED'),
    ('2', 'NEGATIVE'),
    ('3', 'POSITIVE'),
    ('4', 'FALSE_POSITIVE'),
  
)

    
 

class FindingBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PhysicalFindingBase(FindingBase): 

    icdCode = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class LabFindingBase(FindingBase): 

    testName = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DiseaseBase(models.Model): 

    gender = models.CharField(null = False, blank =  True, max_length = 1 , choices = Gender)
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
    relatedDisease = models.ForeignKey('ddx.Disease', related_name='differentialDiagnoses')
        
    
    conditionCategory = models.ForeignKey('ddx.ConditionCategory', related_name='disease')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def relatedDiseaseDisplayName(self):
        return self.relatedDisease.__str__()
    @property   
    def conditionCategoryDisplayName(self):
        return self.conditionCategory.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ConditionFindingBase(models.Model): 

    disease = models.ForeignKey('ddx.Disease', related_name='conditionFinding')
        
    
    falsePositive = models.NullBooleanField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def diseaseDisplayName(self):
        return self.disease.__str__()
    
    
    def __str__(self):
        return self.disease+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ConditionCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DifferentialDxBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    dxCategory = models.ForeignKey('ddx.DxCategory', related_name='differentialDx')
        
    
    finding = models.ForeignKey('ddx.Finding', related_name='differentialDxs')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def dxCategoryDisplayName(self):
        return self.dxCategory.__str__()
    @property   
    def findingDisplayName(self):
        return self.finding.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DxCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientFindingBase(models.Model): 

    finding = models.ForeignKey('ddx.Finding', related_name='patientFinding')
        
    
    patientDiffDx = models.ForeignKey('ddx.PatientDiffDx', related_name='patientFindings')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def findingDisplayName(self):
        return self.finding.__str__()
    @property   
    def patientDiffDxDisplayName(self):
        return self.patientDiffDx.__str__()
    
    
    def __str__(self):
        return self.finding+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientDiffDxBase(models.Model): 

            
        
    
    notes = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.notes 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DxTestBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChronicConditionBase(models.Model): 

    name = models.CharField(null = False, blank =  True, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  