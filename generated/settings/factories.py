
 
 # factories.py
import factory
from . import models



class  SettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Settings
        
        
     

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Setting
        
        
    value = factory.Sequence(lambda n: CharField) 
    
    settingName = factory.SubFactory(settings.SettingNameFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SettingName
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    settingGroup = factory.SubFactory(settings.SettingGroupFactory)
        
    
    defaultValue = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SettingGroup
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 