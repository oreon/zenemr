
 
 # factories.py
import factory
from . import models



class  OrderTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. OrderTemplate
        
        
     

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Order
        
        
    orderTemplate = factory.SubFactory(physicianOrder.OrderTemplateFactory)
        
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 