
 
 # factories.py
import factory
from . import models



class  CodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Code
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    includes = factory.Sequence(lambda n: TextField) 
    
    notIncludedHere = factory.Sequence(lambda n: TextField) 
    
    codeFirst = factory.Sequence(lambda n: TextField) 
    
    section = factory.SubFactory(codes.SectionFactory)
        
    
    notCodedHere = factory.Sequence(lambda n: TextField) 
    
    codeAlso = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChapterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Chapter
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Section
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    chapter = factory.SubFactory(codes.ChapterFactory)
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SimpleCodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SimpleCode
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 