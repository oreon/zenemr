
 
 # factories.py
import factory
from . import models



class  PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Patient
        
        
    firstName = factory.Sequence(lambda n: CharField) 
    
    lastName = factory.Sequence(lambda n: CharField) 
    
    customerType = factory.Sequence(lambda n: CharField) 
    
            
        
    
            
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  VaccinationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Vaccination
        
        
    review = factory.Sequence(lambda n: TextField) 
    
    rating = factory.Sequence(lambda n: PositiveIntegerField) 
    
    vaccine = factory.SubFactory(patients.VaccineFactory)
        
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  EncounterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Encounter
        
        
    reason = factory.Sequence(lambda n: TextField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
    labTests =    models.ManyToManyField("patients.LabTest",  blank=True,  related_name="labTests")
            
        
    
        
    prescription =    models.OneToOneField("prescription.Prescription",  blank=True,  related_name="prescription")
        
    
    admission = factory.SubFactory(admission.AdmissionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  VaccineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Vaccine
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  LabTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. LabTest
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    encounters =    models.ManyToManyField("patients.Encounter",  blank=True,  related_name="encounters")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  TestResultsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. TestResults
        
        
    patient = factory.SubFactory(patients.PatientFactory)
        
    
            
        
    
    labTest = factory.SubFactory(patients.LabTestFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ResultRowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ResultRow
        
        
    testResults = factory.SubFactory(patients.TestResultsFactory)
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    value = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 