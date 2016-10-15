
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'appointments', AppointmentViewSet)
router.register(r'appointmentsWritable', AppointmentWritableViewSet)
router.register(r'appointmentsComplete', AppointmentCompleteViewSet)
router.register(r'appointmentsLookup', AppointmentLookupViewSet)

    
