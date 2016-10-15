
from rest_framework import viewsets
from .serializers import *
    
class UnusualOccurenceViewSet(viewsets.ModelViewSet):
    queryset = UnusualOccurence.objects.all()
    serializer_class = UnusualOccurenceSerializer
    
class UnusualOccurenceLookupViewSet(viewsets.ModelViewSet):
    queryset = UnusualOccurence.objects.all()
    serializer_class = UnusualOccurenceLookupSerializer
    
class UnusualOccurenceCompleteViewSet(UnusualOccurenceViewSet):
    serializer_class = FullUnusualOccurenceSerializer
    
class UnusualOccurenceWritableViewSet(UnusualOccurenceViewSet):
    serializer_class = UnusualOccurenceWritableSerializer    

class OccurenceTypeViewSet(viewsets.ModelViewSet):
    queryset = OccurenceType.objects.all()
    serializer_class = OccurenceTypeSerializer
    
class OccurenceTypeLookupViewSet(viewsets.ModelViewSet):
    queryset = OccurenceType.objects.all()
    serializer_class = OccurenceTypeLookupSerializer
    
class OccurenceTypeCompleteViewSet(OccurenceTypeViewSet):
    serializer_class = FullOccurenceTypeSerializer
    
class OccurenceTypeWritableViewSet(OccurenceTypeViewSet):
    serializer_class = OccurenceTypeWritableSerializer    

  