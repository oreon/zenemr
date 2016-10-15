
from rest_framework import viewsets
from .serializers import *
    
class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    
class FacilityLookupViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilityLookupSerializer
    
class FacilityCompleteViewSet(FacilityViewSet):
    serializer_class = FullFacilitySerializer
    
class FacilityWritableViewSet(FacilityViewSet):
    serializer_class = FacilityWritableSerializer    

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class RoomLookupViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomLookupSerializer
    
class RoomCompleteViewSet(RoomViewSet):
    serializer_class = FullRoomSerializer
    
class RoomWritableViewSet(RoomViewSet):
    serializer_class = RoomWritableSerializer    

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    
class BedLookupViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedLookupSerializer
    
class BedCompleteViewSet(BedViewSet):
    serializer_class = FullBedSerializer
    
class BedWritableViewSet(BedViewSet):
    serializer_class = BedWritableSerializer    

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    
class WardLookupViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardLookupSerializer
    
class WardCompleteViewSet(WardViewSet):
    serializer_class = FullWardSerializer
    
class WardWritableViewSet(WardViewSet):
    serializer_class = WardWritableSerializer    

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    
class RoomTypeLookupViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeLookupSerializer
    
class RoomTypeCompleteViewSet(RoomTypeViewSet):
    serializer_class = FullRoomTypeSerializer
    
class RoomTypeWritableViewSet(RoomTypeViewSet):
    serializer_class = RoomTypeWritableSerializer    

  