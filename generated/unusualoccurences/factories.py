
 
 # factories.py
import factory
from . import models



class  UnusualOccurenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. UnusualOccurence
        
        
    occurenceType = factory.SubFactory(unusualoccurences.OccurenceTypeFactory)
        
    
    category = factory.Sequence(lambda n: CharField) 
    
    severity = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  OccurenceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. OccurenceType
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 