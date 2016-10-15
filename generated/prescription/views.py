
from rest_framework import viewsets
from .serializers import *
    
class PrescriptionTemplateViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionTemplate.objects.all()
    serializer_class = PrescriptionTemplateSerializer
    
class PrescriptionTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionTemplate.objects.all()
    serializer_class = PrescriptionTemplateLookupSerializer
    
class PrescriptionTemplateCompleteViewSet(PrescriptionTemplateViewSet):
    serializer_class = FullPrescriptionTemplateSerializer
    
class PrescriptionTemplateWritableViewSet(PrescriptionTemplateViewSet):
    serializer_class = PrescriptionTemplateWritableSerializer    

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class PrescriptionLookupViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionLookupSerializer
    
class PrescriptionCompleteViewSet(PrescriptionViewSet):
    serializer_class = FullPrescriptionSerializer
    
class PrescriptionWritableViewSet(PrescriptionViewSet):
    serializer_class = PrescriptionWritableSerializer    

class PrescriptionItemViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemSerializer
    
class PrescriptionItemLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemLookupSerializer
    
class PrescriptionItemCompleteViewSet(PrescriptionItemViewSet):
    serializer_class = FullPrescriptionItemSerializer
    
class PrescriptionItemWritableViewSet(PrescriptionItemViewSet):
    serializer_class = PrescriptionItemWritableSerializer    

class PrescriptionItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItemTemplate.objects.all()
    serializer_class = PrescriptionItemTemplateSerializer
    
class PrescriptionItemTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItemTemplate.objects.all()
    serializer_class = PrescriptionItemTemplateLookupSerializer
    
class PrescriptionItemTemplateCompleteViewSet(PrescriptionItemTemplateViewSet):
    serializer_class = FullPrescriptionItemTemplateSerializer
    
class PrescriptionItemTemplateWritableViewSet(PrescriptionItemTemplateViewSet):
    serializer_class = PrescriptionItemTemplateWritableSerializer    

class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
    
class FrequencyLookupViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencyLookupSerializer
    
class FrequencyCompleteViewSet(FrequencyViewSet):
    serializer_class = FullFrequencySerializer
    
class FrequencyWritableViewSet(FrequencyViewSet):
    serializer_class = FrequencyWritableSerializer    

  