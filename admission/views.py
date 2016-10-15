
from rest_framework import viewsets
from .serializers import *
    
class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    
class AdmissionLookupViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionLookupSerializer
    
class AdmissionCompleteViewSet(AdmissionViewSet):
    serializer_class = FullAdmissionSerializer
    
class AdmissionWritableViewSet(AdmissionViewSet):
    serializer_class = AdmissionWritableSerializer    

class BedStayViewSet(viewsets.ModelViewSet):
    queryset = BedStay.objects.all()
    serializer_class = BedStaySerializer
    
class BedStayLookupViewSet(viewsets.ModelViewSet):
    queryset = BedStay.objects.all()
    serializer_class = BedStayLookupSerializer
    
class BedStayCompleteViewSet(BedStayViewSet):
    serializer_class = FullBedStaySerializer
    
class BedStayWritableViewSet(BedStayViewSet):
    serializer_class = BedStayWritableSerializer    

  