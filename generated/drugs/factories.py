
 
 # factories.py
import factory
from . import models



class  AtcDrugFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AtcDrug
        
        
    code = factory.Sequence(lambda n: CharField) 
    
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    parent = factory.SubFactory(drugs.AtcDrugFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Drug
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    absorption = factory.Sequence(lambda n: TextField) 
    
    biotransformation = factory.Sequence(lambda n: TextField) 
    
    atcCodes = factory.Sequence(lambda n: CharField) 
    
    contraIndication = factory.Sequence(lambda n: TextField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    dosageForm = factory.Sequence(lambda n: CharField) 
    
    foodInteractions = factory.Sequence(lambda n: TextField) 
    
    halfLife = factory.Sequence(lambda n: TextField) 
    
    indication = factory.Sequence(lambda n: TextField) 
    
    halfLifeNumberOfHours = factory.Sequence(lambda n: CharField) 
    
    mechanismOfAction = factory.Sequence(lambda n: TextField) 
    
    patientInfo = factory.Sequence(lambda n: TextField) 
    
    pharmacology = factory.Sequence(lambda n: TextField) 
    
            
        
    
    drugCategorys =    models.ManyToManyField("drugs.DrugCategory",  blank=True,  related_name="drugCategorys")
            
        
    
    toxicity = factory.Sequence(lambda n: TextField) 
    
    routeOfElimination = factory.Sequence(lambda n: TextField) 
    
    volumeOfDistribution = factory.Sequence(lambda n: CharField) 
    
    drugBankId = factory.Sequence(lambda n: CharField) 
    
    categories = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugInteractionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DrugInteraction
        
        
    description = factory.Sequence(lambda n: TextField) 
    
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    interactingDrug = factory.SubFactory(drugs.DrugFactory)
        
    
    severity = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DrugCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    drugs =    models.ManyToManyField("drugs.Drug",  blank=True,  related_name="drugs")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 