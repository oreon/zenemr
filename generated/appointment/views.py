
from rest_framework import viewsets
from .serializers import *
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class AppointmentLookupViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentLookupSerializer
    
class AppointmentCompleteViewSet(AppointmentViewSet):
    serializer_class = FullAppointmentSerializer
    
class AppointmentWritableViewSet(AppointmentViewSet):
    serializer_class = AppointmentWritableSerializer    

  