
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'facilitys', FacilityViewSet)
router.register(r'facilitysWritable', FacilityWritableViewSet)
router.register(r'facilitysComplete', FacilityCompleteViewSet)
router.register(r'facilitysLookup', FacilityLookupViewSet)
  
router.register(r'rooms', RoomViewSet)
router.register(r'roomsWritable', RoomWritableViewSet)
router.register(r'roomsComplete', RoomCompleteViewSet)
router.register(r'roomsLookup', RoomLookupViewSet)
  
router.register(r'beds', BedViewSet)
router.register(r'bedsWritable', BedWritableViewSet)
router.register(r'bedsComplete', BedCompleteViewSet)
router.register(r'bedsLookup', BedLookupViewSet)
  
router.register(r'wards', WardViewSet)
router.register(r'wardsWritable', WardWritableViewSet)
router.register(r'wardsComplete', WardCompleteViewSet)
router.register(r'wardsLookup', WardLookupViewSet)
  
router.register(r'roomTypes', RoomTypeViewSet)
router.register(r'roomTypesWritable', RoomTypeWritableViewSet)
router.register(r'roomTypesComplete', RoomTypeCompleteViewSet)
router.register(r'roomTypesLookup', RoomTypeLookupViewSet)

    
