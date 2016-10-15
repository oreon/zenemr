
from rest_framework import viewsets
from .serializers import *
    
class FindingViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class FindingLookupViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingLookupSerializer
    
class FindingCompleteViewSet(FindingViewSet):
    serializer_class = FullFindingSerializer
    
class FindingWritableViewSet(FindingViewSet):
    serializer_class = FindingWritableSerializer    

class PhysicalFindingViewSet(viewsets.ModelViewSet):
    queryset = PhysicalFinding.objects.all()
    serializer_class = PhysicalFindingSerializer
    
class PhysicalFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = PhysicalFinding.objects.all()
    serializer_class = PhysicalFindingLookupSerializer
    
class PhysicalFindingCompleteViewSet(PhysicalFindingViewSet):
    serializer_class = FullPhysicalFindingSerializer
    
class PhysicalFindingWritableViewSet(PhysicalFindingViewSet):
    serializer_class = PhysicalFindingWritableSerializer    

class LabFindingViewSet(viewsets.ModelViewSet):
    queryset = LabFinding.objects.all()
    serializer_class = LabFindingSerializer
    
class LabFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = LabFinding.objects.all()
    serializer_class = LabFindingLookupSerializer
    
class LabFindingCompleteViewSet(LabFindingViewSet):
    serializer_class = FullLabFindingSerializer
    
class LabFindingWritableViewSet(LabFindingViewSet):
    serializer_class = LabFindingWritableSerializer    

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    
class DiseaseLookupViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseLookupSerializer
    
class DiseaseCompleteViewSet(DiseaseViewSet):
    serializer_class = FullDiseaseSerializer
    
class DiseaseWritableViewSet(DiseaseViewSet):
    serializer_class = DiseaseWritableSerializer    

class ConditionFindingViewSet(viewsets.ModelViewSet):
    queryset = ConditionFinding.objects.all()
    serializer_class = ConditionFindingSerializer
    
class ConditionFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = ConditionFinding.objects.all()
    serializer_class = ConditionFindingLookupSerializer
    
class ConditionFindingCompleteViewSet(ConditionFindingViewSet):
    serializer_class = FullConditionFindingSerializer
    
class ConditionFindingWritableViewSet(ConditionFindingViewSet):
    serializer_class = ConditionFindingWritableSerializer    

class ConditionCategoryViewSet(viewsets.ModelViewSet):
    queryset = ConditionCategory.objects.all()
    serializer_class = ConditionCategorySerializer
    
class ConditionCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = ConditionCategory.objects.all()
    serializer_class = ConditionCategoryLookupSerializer
    
class ConditionCategoryCompleteViewSet(ConditionCategoryViewSet):
    serializer_class = FullConditionCategorySerializer
    
class ConditionCategoryWritableViewSet(ConditionCategoryViewSet):
    serializer_class = ConditionCategoryWritableSerializer    

class DifferentialDxViewSet(viewsets.ModelViewSet):
    queryset = DifferentialDx.objects.all()
    serializer_class = DifferentialDxSerializer
    
class DifferentialDxLookupViewSet(viewsets.ModelViewSet):
    queryset = DifferentialDx.objects.all()
    serializer_class = DifferentialDxLookupSerializer
    
class DifferentialDxCompleteViewSet(DifferentialDxViewSet):
    serializer_class = FullDifferentialDxSerializer
    
class DifferentialDxWritableViewSet(DifferentialDxViewSet):
    serializer_class = DifferentialDxWritableSerializer    

class DxCategoryViewSet(viewsets.ModelViewSet):
    queryset = DxCategory.objects.all()
    serializer_class = DxCategorySerializer
    
class DxCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = DxCategory.objects.all()
    serializer_class = DxCategoryLookupSerializer
    
class DxCategoryCompleteViewSet(DxCategoryViewSet):
    serializer_class = FullDxCategorySerializer
    
class DxCategoryWritableViewSet(DxCategoryViewSet):
    serializer_class = DxCategoryWritableSerializer    

class PatientFindingViewSet(viewsets.ModelViewSet):
    queryset = PatientFinding.objects.all()
    serializer_class = PatientFindingSerializer
    
class PatientFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = PatientFinding.objects.all()
    serializer_class = PatientFindingLookupSerializer
    
class PatientFindingCompleteViewSet(PatientFindingViewSet):
    serializer_class = FullPatientFindingSerializer
    
class PatientFindingWritableViewSet(PatientFindingViewSet):
    serializer_class = PatientFindingWritableSerializer    

class PatientDiffDxViewSet(viewsets.ModelViewSet):
    queryset = PatientDiffDx.objects.all()
    serializer_class = PatientDiffDxSerializer
    
class PatientDiffDxLookupViewSet(viewsets.ModelViewSet):
    queryset = PatientDiffDx.objects.all()
    serializer_class = PatientDiffDxLookupSerializer
    
class PatientDiffDxCompleteViewSet(PatientDiffDxViewSet):
    serializer_class = FullPatientDiffDxSerializer
    
class PatientDiffDxWritableViewSet(PatientDiffDxViewSet):
    serializer_class = PatientDiffDxWritableSerializer    

class DxTestViewSet(viewsets.ModelViewSet):
    queryset = DxTest.objects.all()
    serializer_class = DxTestSerializer
    
class DxTestLookupViewSet(viewsets.ModelViewSet):
    queryset = DxTest.objects.all()
    serializer_class = DxTestLookupSerializer
    
class DxTestCompleteViewSet(DxTestViewSet):
    serializer_class = FullDxTestSerializer
    
class DxTestWritableViewSet(DxTestViewSet):
    serializer_class = DxTestWritableSerializer    

class ChronicConditionViewSet(viewsets.ModelViewSet):
    queryset = ChronicCondition.objects.all()
    serializer_class = ChronicConditionSerializer
    
class ChronicConditionLookupViewSet(viewsets.ModelViewSet):
    queryset = ChronicCondition.objects.all()
    serializer_class = ChronicConditionLookupSerializer
    
class ChronicConditionCompleteViewSet(ChronicConditionViewSet):
    serializer_class = FullChronicConditionSerializer
    
class ChronicConditionWritableViewSet(ChronicConditionViewSet):
    serializer_class = ChronicConditionWritableSerializer    

  