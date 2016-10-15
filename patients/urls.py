
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'drugs', DrugViewSet)
router.register(r'drugsWritable', DrugWritableViewSet)
router.register(r'drugsComplete', DrugCompleteViewSet)
router.register(r'drugsLookup', DrugLookupViewSet)
  
router.register(r'categorys', CategoryViewSet)
router.register(r'categorysWritable', CategoryWritableViewSet)
router.register(r'categorysComplete', CategoryCompleteViewSet)
router.register(r'categorysLookup', CategoryLookupViewSet)
  
router.register(r'patients', PatientViewSet)
router.register(r'patientsWritable', PatientWritableViewSet)
router.register(r'patientsComplete', PatientCompleteViewSet)
router.register(r'patientsLookup', PatientLookupViewSet)
  
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'prescriptionsWritable', PrescriptionWritableViewSet)
router.register(r'prescriptionsComplete', PrescriptionCompleteViewSet)
router.register(r'prescriptionsLookup', PrescriptionLookupViewSet)
  
router.register(r'prescriptionItems', PrescriptionItemViewSet)
router.register(r'prescriptionItemsWritable', PrescriptionItemWritableViewSet)
router.register(r'prescriptionItemsComplete', PrescriptionItemCompleteViewSet)
router.register(r'prescriptionItemsLookup', PrescriptionItemLookupViewSet)
  
router.register(r'employees', EmployeeViewSet)
router.register(r'employeesWritable', EmployeeWritableViewSet)
router.register(r'employeesComplete', EmployeeCompleteViewSet)
router.register(r'employeesLookup', EmployeeLookupViewSet)
  
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

    
