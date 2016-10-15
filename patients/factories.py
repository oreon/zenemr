# 
#  
#  # factories.py
# import factory
# from . import models
# 
# 
# 
# class  DrugFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Drug
#         
#         
#     name = factory.Sequence(lambda n: CharField) 
#     
#     price = factory.Sequence(lambda n: DecimalField) 
#     
#     image = factory.Sequence(lambda n: ImageField) 
#     
#     categorys =    models.ManyToManyField("patients.Category",  blank=True,  related_name="categorys")
#             
#         
#     
#     displayTill = factory.Sequence(lambda n: DateField) 
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Category
#         
#         
#     drugs =    models.ManyToManyField("patients.Drug",  blank=True,  related_name="drugs")
#             
#         
#     
#     name = factory.Sequence(lambda n: CharField) 
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  PatientFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Patient
#         
#         
#     firstName = factory.Sequence(lambda n: CharField) 
#     
#     lastName = factory.Sequence(lambda n: CharField) 
#     
#     customerType = factory.Sequence(lambda n: CharField) 
#     
#             
#         
#     
#             
#         
#     
#             
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  PrescriptionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Prescription
#         
#         
#             
#         
#     
#     notes = factory.Sequence(lambda n: TextField) 
#     
#     isCurrent = factory.Sequence(lambda n: NullBooleanField) 
#     
#         
#     encounter =    models.OneToOneField("patients.Encounter",  blank=True,  related_name="encounter")
#         
#     
#     patient = factory.SubFactory(patients.PatientFactory)
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  PrescriptionItemFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. PrescriptionItem
#         
#         
#     prescription = factory.SubFactory(patients.PrescriptionFactory)
#         
#     
#     qty = factory.Sequence(lambda n: PositiveIntegerField) 
#     
#     drug = factory.SubFactory(patients.DrugFactory)
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  EmployeeFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Employee
#         
#         
#     firstName = factory.Sequence(lambda n: CharField) 
#     
#     lastName = factory.Sequence(lambda n: CharField) 
#     
#     active = factory.Sequence(lambda n: NullBooleanField) 
#     
#         
#     appUser =    models.OneToOneField("users.AppUser",  blank=True,  related_name="appUser")
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  VaccinationFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Vaccination
#         
#         
#     review = factory.Sequence(lambda n: TextField) 
#     
#     rating = factory.Sequence(lambda n: PositiveIntegerField) 
#     
#     vaccine = factory.SubFactory(patients.VaccineFactory)
#         
#     
#     patient = factory.SubFactory(patients.PatientFactory)
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  EncounterFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Encounter
#         
#         
#     reason = factory.Sequence(lambda n: TextField) 
#     
#         
#     prescription =    models.OneToOneField("patients.Prescription",  blank=True,  related_name="prescription")
#         
#     
#     patient = factory.SubFactory(patients.PatientFactory)
#         
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
# class  VaccineFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models. Vaccine
#         
#         
#     name = factory.Sequence(lambda n: CharField) 
#     
#  
# 
#     #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     #group = factory.SubFactory(GroupFactory)
# 
# 
# 
#  