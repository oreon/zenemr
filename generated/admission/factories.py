
 
 # factories.py
import factory
from . import models



class  AdmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Admission
        
        
    admissionNote = factory.Sequence(lambda n: TextField) 
    
    dischargeDate = factory.Sequence(lambda n: DateField) 
    
    dischargeNote = factory.Sequence(lambda n: TextField) 
    
    dischargeCode = factory.Sequence(lambda n: CharField) 
    
    currentBed = factory.Sequence(lambda n: CharField) 
    
    isCurrent = factory.Sequence(lambda n: NullBooleanField) 
    
    invoice = factory.SubFactory(billing.InvoiceFactory)
        
    
            
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  BedStayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. BedStay
        
        
    fromDate = factory.Sequence(lambda n: DateField) 
    
    toDate = factory.Sequence(lambda n: DateField) 
    
    admission = factory.SubFactory(admission.AdmissionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 