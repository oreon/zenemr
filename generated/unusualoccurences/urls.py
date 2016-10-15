
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'unusualOccurences', UnusualOccurenceViewSet)
router.register(r'unusualOccurencesWritable', UnusualOccurenceWritableViewSet)
router.register(r'unusualOccurencesComplete', UnusualOccurenceCompleteViewSet)
router.register(r'unusualOccurencesLookup', UnusualOccurenceLookupViewSet)
  
router.register(r'occurenceTypes', OccurenceTypeViewSet)
router.register(r'occurenceTypesWritable', OccurenceTypeWritableViewSet)
router.register(r'occurenceTypesComplete', OccurenceTypeCompleteViewSet)
router.register(r'occurenceTypesLookup', OccurenceTypeLookupViewSet)

    
