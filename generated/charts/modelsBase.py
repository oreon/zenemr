
from django.db import models

    
TimeEnumeration = (
    ('0', 'HOUR'),
    ('1', 'DAY'),
    ('2', 'WEEK'),
    ('3', 'MONTH'),
    ('4', 'YEAR'),
  
)

    
 

class AppliedChartBase(models.Model): 

    chart = models.ForeignKey('charts.Chart', related_name='appliedChart')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartDisplayName(self):
        return self.chart.__str__()
    
    
    def __str__(self):
        return self.chart+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartBase(models.Model): 

            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    chronicCondition = models.ForeignKey('ddx.ChronicCondition', related_name='charts')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chronicConditionDisplayName(self):
        return self.chronicCondition.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartItemBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    chart = models.ForeignKey('charts.Chart', related_name='chartItems')
        
    
    frequencyPeriod = models.CharField(null = False, blank =  True, max_length = 1 , choices = TimeEnumeration)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartDisplayName(self):
        return self.chart.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartProcedureBase(models.Model): 

    chartItem = models.ForeignKey('charts.ChartItem', related_name='chartProcedure')
        
    
    dueDate = models.DateField(null = False, blank =  True, )
    
    datePerformed = models.DateField(null = False, blank =  True, )
    
    remarks = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartItemDisplayName(self):
        return self.chartItem.__str__()
    
    
    def __str__(self):
        return self.remarks 
        
    class Meta:
        abstract = True
        
    
      
        

  