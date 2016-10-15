
from rest_framework import viewsets
from .serializers import *
    
class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    
class DrugLookupViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugLookupSerializer
    
class DrugCompleteViewSet(DrugViewSet):
    serializer_class = FullDrugSerializer
    
class DrugWritableViewSet(DrugViewSet):
    serializer_class = DrugWritableSerializer    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryLookupSerializer
    
class CategoryCompleteViewSet(CategoryViewSet):
    serializer_class = FullCategorySerializer
    
class CategoryWritableViewSet(CategoryViewSet):
    serializer_class = CategoryWritableSerializer    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class PatientLookupViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientLookupSerializer
    
class PatientCompleteViewSet(PatientViewSet):
    serializer_class = FullPatientSerializer
    
class PatientWritableViewSet(PatientViewSet):
    serializer_class = PatientWritableSerializer    

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class PrescriptionLookupViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionLookupSerializer
    
class PrescriptionCompleteViewSet(PrescriptionViewSet):
    serializer_class = FullPrescriptionSerializer
    
class PrescriptionWritableViewSet(PrescriptionViewSet):
    serializer_class = PrescriptionWritableSerializer    

class PrescriptionItemViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemSerializer
    
class PrescriptionItemLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemLookupSerializer
    
class PrescriptionItemCompleteViewSet(PrescriptionItemViewSet):
    serializer_class = FullPrescriptionItemSerializer
    
class PrescriptionItemWritableViewSet(PrescriptionItemViewSet):
    serializer_class = PrescriptionItemWritableSerializer    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeLookupViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeLookupSerializer
    
class EmployeeCompleteViewSet(EmployeeViewSet):
    serializer_class = FullEmployeeSerializer
    
class EmployeeWritableViewSet(EmployeeViewSet):
    serializer_class = EmployeeWritableSerializer    

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    
class VaccinationLookupViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationLookupSerializer
    
class VaccinationCompleteViewSet(VaccinationViewSet):
    serializer_class = FullVaccinationSerializer
    
class VaccinationWritableViewSet(VaccinationViewSet):
    serializer_class = VaccinationWritableSerializer    

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    
class EncounterLookupViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterLookupSerializer
    
class EncounterCompleteViewSet(EncounterViewSet):
    serializer_class = FullEncounterSerializer
    
class EncounterWritableViewSet(EncounterViewSet):
    serializer_class = EncounterWritableSerializer    

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    
class VaccineLookupViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineLookupSerializer
    
class VaccineCompleteViewSet(VaccineViewSet):
    serializer_class = FullVaccineSerializer
    
class VaccineWritableViewSet(VaccineViewSet):
    serializer_class = VaccineWritableSerializer    

  