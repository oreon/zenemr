
 
 # factories.py
import factory
from . import models



class  FindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Finding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PhysicalFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PhysicalFinding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    icdCode = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  LabFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. LabFinding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    testName = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Disease
        
        
    gender = factory.Sequence(lambda n: CharField) 
    
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    relatedDisease = factory.SubFactory(ddx.DiseaseFactory)
        
    
    conditionCategory = factory.SubFactory(ddx.ConditionCategoryFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ConditionFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ConditionFinding
        
        
    disease = factory.SubFactory(ddx.DiseaseFactory)
        
    
    falsePositive = factory.Sequence(lambda n: NullBooleanField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ConditionCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ConditionCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DifferentialDxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DifferentialDx
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    dxCategory = factory.SubFactory(ddx.DxCategoryFactory)
        
    
    finding = factory.SubFactory(ddx.FindingFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DxCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DxCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PatientFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PatientFinding
        
        
    finding = factory.SubFactory(ddx.FindingFactory)
        
    
    patientDiffDx = factory.SubFactory(ddx.PatientDiffDxFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PatientDiffDxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PatientDiffDx
        
        
            
        
    
    notes = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DxTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DxTest
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChronicConditionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChronicCondition
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 