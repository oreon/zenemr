
 
 # factories.py
import factory
from . import models



class  EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Employee
        
        
    firstName = factory.Sequence(lambda n: CharField) 
    
    lastName = factory.Sequence(lambda n: CharField) 
    
    active = factory.Sequence(lambda n: NullBooleanField) 
    
        
    appUser =    models.OneToOneField("users.AppUser",  blank=True,  related_name="appUser")
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 