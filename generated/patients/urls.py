
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'patients', PatientViewSet)
router.register(r'patientsWritable', PatientWritableViewSet)
router.register(r'patientsComplete', PatientCompleteViewSet)
router.register(r'patientsLookup', PatientLookupViewSet)
  
router.register(r'vaccinations', VaccinationViewSet)
router.register(r'vaccinationsWritable', VaccinationWritableViewSet)
router.register(r'vaccinationsComplete', VaccinationCompleteViewSet)
router.register(r'vaccinationsLookup', VaccinationLookupViewSet)
  
router.register(r'encounters', EncounterViewSet)
router.register(r'encountersWritable', EncounterWritableViewSet)
router.register(r'encountersComplete', EncounterCompleteViewSet)
router.register(r'encountersLookup', EncounterLookupViewSet)
  
router.register(r'vaccines', VaccineViewSet)
router.register(r'vaccinesWritable', VaccineWritableViewSet)
router.register(r'vaccinesComplete', VaccineCompleteViewSet)
router.register(r'vaccinesLookup', VaccineLookupViewSet)
  
router.register(r'labTests', LabTestViewSet)
router.register(r'labTestsWritable', LabTestWritableViewSet)
router.register(r'labTestsComplete', LabTestCompleteViewSet)
router.register(r'labTestsLookup', LabTestLookupViewSet)
  
router.register(r'testResultses', TestResultsViewSet)
router.register(r'testResultsesWritable', TestResultsWritableViewSet)
router.register(r'testResultsesComplete', TestResultsCompleteViewSet)
router.register(r'testResultsesLookup', TestResultsLookupViewSet)
  
router.register(r'resultRows', ResultRowViewSet)
router.register(r'resultRowsWritable', ResultRowWritableViewSet)
router.register(r'resultRowsComplete', ResultRowCompleteViewSet)
router.register(r'resultRowsLookup', ResultRowLookupViewSet)

    
