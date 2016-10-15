
from django.db import models


    
 

class FacilityBase(models.Model): 

    name = models.CharField(null = False, blank =  True, max_length=30)
    
            
        
    
    isResidential = models.NullBooleanField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class RoomBase(models.Model): 

            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    roomType = models.ForeignKey('facility.RoomType', related_name='room')
        
    
    ward = models.ForeignKey('facility.Ward', related_name='rooms')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def roomTypeDisplayName(self):
        return self.roomType.__str__()
    @property   
    def wardDisplayName(self):
        return self.ward.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class BedBase(models.Model): 

    room = models.ForeignKey('facility.Room', related_name='beds')
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def roomDisplayName(self):
        return self.room.__str__()
    
    
    def __str__(self):
        return room.getName() + " " + name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class WardBase(models.Model): 

    facility = models.ForeignKey('facility.Facility', related_name='wards')
        
    
            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    gender = models.CharField(null = False, blank =  True, max_length = 1 , choices = Gender)
    
    maxAge = models.PositiveIntegerField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def facilityDisplayName(self):
        return self.facility.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class RoomTypeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
    rate = models.CharField(null = False, blank =  True, )
    
    numberOfBeds = models.PositiveIntegerField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        

  