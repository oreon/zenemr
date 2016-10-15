
 
 # factories.py
import factory
from . import models



class  FacilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Facility
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    isResidential = factory.Sequence(lambda n: NullBooleanField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Room
        
        
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    roomType = factory.SubFactory(facility.RoomTypeFactory)
        
    
    ward = factory.SubFactory(facility.WardFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  BedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Bed
        
        
    room = factory.SubFactory(facility.RoomFactory)
        
    
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  WardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Ward
        
        
    facility = factory.SubFactory(facility.FacilityFactory)
        
    
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    gender = factory.Sequence(lambda n: CharField) 
    
    maxAge = factory.Sequence(lambda n: PositiveIntegerField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  RoomTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. RoomType
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    rate = factory.Sequence(lambda n: CharField) 
    
    numberOfBeds = factory.Sequence(lambda n: PositiveIntegerField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 