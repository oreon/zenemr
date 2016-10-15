
from django.db import models


    
 

class EmployeeBase(PersonBase): 

    active = models.NullBooleanField(null = False, blank =  True, )
    
        
    appUser =    models.OneToOneField("users.AppUser",  null = True,blank=True,  related_name="appUser")
        
    
 
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
        
    
      
        

  