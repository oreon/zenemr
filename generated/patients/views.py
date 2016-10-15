
from rest_framework import viewsets
from .serializers import *
    
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

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer
    
class LabTestLookupViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestLookupSerializer
    
class LabTestCompleteViewSet(LabTestViewSet):
    serializer_class = FullLabTestSerializer
    
class LabTestWritableViewSet(LabTestViewSet):
    serializer_class = LabTestWritableSerializer    

class TestResultsViewSet(viewsets.ModelViewSet):
    queryset = TestResults.objects.all()
    serializer_class = TestResultsSerializer
    
class TestResultsLookupViewSet(viewsets.ModelViewSet):
    queryset = TestResults.objects.all()
    serializer_class = TestResultsLookupSerializer
    
class TestResultsCompleteViewSet(TestResultsViewSet):
    serializer_class = FullTestResultsSerializer
    
class TestResultsWritableViewSet(TestResultsViewSet):
    serializer_class = TestResultsWritableSerializer    

class ResultRowViewSet(viewsets.ModelViewSet):
    queryset = ResultRow.objects.all()
    serializer_class = ResultRowSerializer
    
class ResultRowLookupViewSet(viewsets.ModelViewSet):
    queryset = ResultRow.objects.all()
    serializer_class = ResultRowLookupSerializer
    
class ResultRowCompleteViewSet(ResultRowViewSet):
    serializer_class = FullResultRowSerializer
    
class ResultRowWritableViewSet(ResultRowViewSet):
    serializer_class = ResultRowWritableSerializer    

  