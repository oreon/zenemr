
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'findings', FindingViewSet)
router.register(r'findingsWritable', FindingWritableViewSet)
router.register(r'findingsComplete', FindingCompleteViewSet)
router.register(r'findingsLookup', FindingLookupViewSet)
  
router.register(r'physicalFindings', PhysicalFindingViewSet)
router.register(r'physicalFindingsWritable', PhysicalFindingWritableViewSet)
router.register(r'physicalFindingsComplete', PhysicalFindingCompleteViewSet)
router.register(r'physicalFindingsLookup', PhysicalFindingLookupViewSet)
  
router.register(r'labFindings', LabFindingViewSet)
router.register(r'labFindingsWritable', LabFindingWritableViewSet)
router.register(r'labFindingsComplete', LabFindingCompleteViewSet)
router.register(r'labFindingsLookup', LabFindingLookupViewSet)
  
router.register(r'diseases', DiseaseViewSet)
router.register(r'diseasesWritable', DiseaseWritableViewSet)
router.register(r'diseasesComplete', DiseaseCompleteViewSet)
router.register(r'diseasesLookup', DiseaseLookupViewSet)
  
router.register(r'conditionFindings', ConditionFindingViewSet)
router.register(r'conditionFindingsWritable', ConditionFindingWritableViewSet)
router.register(r'conditionFindingsComplete', ConditionFindingCompleteViewSet)
router.register(r'conditionFindingsLookup', ConditionFindingLookupViewSet)
  
router.register(r'conditionCategorys', ConditionCategoryViewSet)
router.register(r'conditionCategorysWritable', ConditionCategoryWritableViewSet)
router.register(r'conditionCategorysComplete', ConditionCategoryCompleteViewSet)
router.register(r'conditionCategorysLookup', ConditionCategoryLookupViewSet)
  
router.register(r'differentialDxs', DifferentialDxViewSet)
router.register(r'differentialDxsWritable', DifferentialDxWritableViewSet)
router.register(r'differentialDxsComplete', DifferentialDxCompleteViewSet)
router.register(r'differentialDxsLookup', DifferentialDxLookupViewSet)
  
router.register(r'dxCategorys', DxCategoryViewSet)
router.register(r'dxCategorysWritable', DxCategoryWritableViewSet)
router.register(r'dxCategorysComplete', DxCategoryCompleteViewSet)
router.register(r'dxCategorysLookup', DxCategoryLookupViewSet)
  
router.register(r'patientFindings', PatientFindingViewSet)
router.register(r'patientFindingsWritable', PatientFindingWritableViewSet)
router.register(r'patientFindingsComplete', PatientFindingCompleteViewSet)
router.register(r'patientFindingsLookup', PatientFindingLookupViewSet)
  
router.register(r'patientDiffDxs', PatientDiffDxViewSet)
router.register(r'patientDiffDxsWritable', PatientDiffDxWritableViewSet)
router.register(r'patientDiffDxsComplete', PatientDiffDxCompleteViewSet)
router.register(r'patientDiffDxsLookup', PatientDiffDxLookupViewSet)
  
router.register(r'dxTests', DxTestViewSet)
router.register(r'dxTestsWritable', DxTestWritableViewSet)
router.register(r'dxTestsComplete', DxTestCompleteViewSet)
router.register(r'dxTestsLookup', DxTestLookupViewSet)
  
router.register(r'chronicConditions', ChronicConditionViewSet)
router.register(r'chronicConditionsWritable', ChronicConditionWritableViewSet)
router.register(r'chronicConditionsComplete', ChronicConditionCompleteViewSet)
router.register(r'chronicConditionsLookup', ChronicConditionLookupViewSet)

    
