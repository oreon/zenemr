
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'admissions', AdmissionViewSet)
router.register(r'admissionsWritable', AdmissionWritableViewSet)
router.register(r'admissionsComplete', AdmissionCompleteViewSet)
router.register(r'admissionsLookup', AdmissionLookupViewSet)
  
router.register(r'bedStays', BedStayViewSet)
router.register(r'bedStaysWritable', BedStayWritableViewSet)
router.register(r'bedStaysComplete', BedStayCompleteViewSet)
router.register(r'bedStaysLookup', BedStayLookupViewSet)

    
