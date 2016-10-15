
from django.db import models


    
 

class SettingsBase(models.Model): 

 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.Empty class - no display name possible 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingBase(models.Model): 

    value = models.CharField(null = False, blank =  False, max_length=30)
    
    settingName = models.ForeignKey('settings.SettingName', related_name='setting')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def settingNameDisplayName(self):
        return self.settingName.__str__()
    
    
    def __str__(self):
        return self.value 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingNameBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    settingGroup = models.ForeignKey('settings.SettingGroup', related_name='settingNames')
        
    
    defaultValue = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def settingGroupDisplayName(self):
        return self.settingGroup.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingGroupBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  