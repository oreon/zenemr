
 
 # factories.py
import factory
from . import models



class  InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Invoice
        
        
            
        
    
    notes = factory.Sequence(lambda n: CharField) 
    
    totalAmount = factory.Sequence(lambda n: DecimalField) 
    
    paidAmount = factory.Sequence(lambda n: DecimalField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Service
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    price = factory.Sequence(lambda n: DecimalField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  InvoiceItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. InvoiceItem
        
        
    units = factory.Sequence(lambda n: PositiveIntegerField) 
    
    service = factory.SubFactory(billing.ServiceFactory)
        
    
    invoice = factory.SubFactory(billing.InvoiceFactory)
        
    
    appliedPrice = factory.Sequence(lambda n: DecimalField) 
    
    total = factory.Sequence(lambda n: DecimalField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 