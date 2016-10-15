
from django.db import models


    
 

class AppointmentBase(models.Model): 

    start = models.DateTimeField(null = False, blank =  True, )
    
    end = models.DateTimeField(null = False, blank =  True, )
    
    remarks = models.TextField(null = False, blank =  True, )
    
    units = models.PositiveIntegerField(null = False, blank =  True, )
    
    patient = models.ForeignKey('patients.Patient', related_name='appointment')
        
    
    employee = models.ForeignKey('employees.Employee', related_name='appointment')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def employeeDisplayName(self):
        return self.employee.__str__()
    
    
    def __str__(self):
        return self.remarks 
        
    class Meta:
        abstract = True
        
    
      
        

  