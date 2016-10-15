
from rest_framework import viewsets
from .serializers import *
    
class AtcDrugViewSet(viewsets.ModelViewSet):
    queryset = AtcDrug.objects.all()
    serializer_class = AtcDrugSerializer
    
class AtcDrugLookupViewSet(viewsets.ModelViewSet):
    queryset = AtcDrug.objects.all()
    serializer_class = AtcDrugLookupSerializer
    
class AtcDrugCompleteViewSet(AtcDrugViewSet):
    serializer_class = FullAtcDrugSerializer
    
class AtcDrugWritableViewSet(AtcDrugViewSet):
    serializer_class = AtcDrugWritableSerializer    

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    
class DrugLookupViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugLookupSerializer
    
class DrugCompleteViewSet(DrugViewSet):
    serializer_class = FullDrugSerializer
    
class DrugWritableViewSet(DrugViewSet):
    serializer_class = DrugWritableSerializer    

class DrugInteractionViewSet(viewsets.ModelViewSet):
    queryset = DrugInteraction.objects.all()
    serializer_class = DrugInteractionSerializer
    
class DrugInteractionLookupViewSet(viewsets.ModelViewSet):
    queryset = DrugInteraction.objects.all()
    serializer_class = DrugInteractionLookupSerializer
    
class DrugInteractionCompleteViewSet(DrugInteractionViewSet):
    serializer_class = FullDrugInteractionSerializer
    
class DrugInteractionWritableViewSet(DrugInteractionViewSet):
    serializer_class = DrugInteractionWritableSerializer    

class DrugCategoryViewSet(viewsets.ModelViewSet):
    queryset = DrugCategory.objects.all()
    serializer_class = DrugCategorySerializer
    
class DrugCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = DrugCategory.objects.all()
    serializer_class = DrugCategoryLookupSerializer
    
class DrugCategoryCompleteViewSet(DrugCategoryViewSet):
    serializer_class = FullDrugCategorySerializer
    
class DrugCategoryWritableViewSet(DrugCategoryViewSet):
    serializer_class = DrugCategoryWritableSerializer    

  