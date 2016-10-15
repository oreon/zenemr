
 
 # factories.py
import factory
from . import models



class  AppliedChartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AppliedChart
        
        
    chart = factory.SubFactory(charts.ChartFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Chart
        
        
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    chronicCondition = factory.SubFactory(ddx.ChronicConditionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChartItem
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    chart = factory.SubFactory(charts.ChartFactory)
        
    
    frequencyPeriod = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartProcedureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChartProcedure
        
        
    chartItem = factory.SubFactory(charts.ChartItemFactory)
        
    
    dueDate = factory.Sequence(lambda n: DateField) 
    
    datePerformed = factory.Sequence(lambda n: DateField) 
    
    remarks = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 