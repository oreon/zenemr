
 
 # factories.py
import factory
from . import models



class  PrescriptionTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionTemplate
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    directivesForPatient = factory.Sequence(lambda n: TextField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Prescription
        
        
            
        
    
    active = factory.Sequence(lambda n: NullBooleanField) 
    
    directivesForPatient = factory.Sequence(lambda n: TextField) 
    
    drugs = factory.Sequence(lambda n: CharField) 
    
    startDate = factory.Sequence(lambda n: DateField) 
    
    endDate = factory.Sequence(lambda n: DateField) 
    
        
    encounter =    models.OneToOneField("patients.Encounter",  blank=True,  related_name="encounter")
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionItem
        
        
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    qty = factory.Sequence(lambda n: CharField) 
    
    strength = factory.Sequence(lambda n: CharField) 
    
    prescription = factory.SubFactory(prescription.PrescriptionFactory)
        
    
    route = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    frequency = factory.SubFactory(prescription.FrequencyFactory)
        
    
    remarks = factory.Sequence(lambda n: CharField) 
    
    brandName = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionItemTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionItemTemplate
        
        
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    qty = factory.Sequence(lambda n: CharField) 
    
    frequency = factory.SubFactory(prescription.FrequencyFactory)
        
    
    strength = factory.Sequence(lambda n: CharField) 
    
    route = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    remarks = factory.Sequence(lambda n: CharField) 
    
    brandName = factory.Sequence(lambda n: CharField) 
    
    prescriptionTemplate = factory.SubFactory(prescription.PrescriptionTemplateFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  FrequencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Frequency
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    qtyPerDay = factory.Sequence(lambda n: PositiveIntegerField) 
    
    remarkts = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 