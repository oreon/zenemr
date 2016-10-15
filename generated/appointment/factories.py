
 
 # factories.py
import factory
from . import models



class  AppointmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Appointment
        
        
    start = factory.Sequence(lambda n: DateTimeField) 
    
    end = factory.Sequence(lambda n: DateTimeField) 
    
    remarks = factory.Sequence(lambda n: TextField) 
    
    units = factory.Sequence(lambda n: PositiveIntegerField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
    employee = factory.SubFactory(employees.EmployeeFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 