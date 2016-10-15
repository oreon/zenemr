
from django.db import models


    
 

class CodeBase(AbstractCodeBase): 

    includes = models.TextField(null = False, blank =  True, )
    
    notIncludedHere = models.TextField(null = False, blank =  True, )
    
    codeFirst = models.TextField(null = False, blank =  True, )
    
    section = models.ForeignKey('codes.Section', related_name='codes')
        
    
    notCodedHere = models.TextField(null = False, blank =  True, )
    
    codeAlso = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def sectionDisplayName(self):
        return self.section.__str__()
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChapterBase(AbstractCodeBase): 

            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SectionBase(AbstractCodeBase): 

    chapter = models.ForeignKey('codes.Chapter', related_name='sections')
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chapterDisplayName(self):
        return self.chapter.__str__()
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AbstractCodeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SimpleCodeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  