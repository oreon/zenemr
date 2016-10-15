
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'atcDrugs', AtcDrugViewSet)
router.register(r'atcDrugsWritable', AtcDrugWritableViewSet)
router.register(r'atcDrugsComplete', AtcDrugCompleteViewSet)
router.register(r'atcDrugsLookup', AtcDrugLookupViewSet)
  
router.register(r'drugs', DrugViewSet)
router.register(r'drugsWritable', DrugWritableViewSet)
router.register(r'drugsComplete', DrugCompleteViewSet)
router.register(r'drugsLookup', DrugLookupViewSet)
  
router.register(r'drugInteractions', DrugInteractionViewSet)
router.register(r'drugInteractionsWritable', DrugInteractionWritableViewSet)
router.register(r'drugInteractionsComplete', DrugInteractionCompleteViewSet)
router.register(r'drugInteractionsLookup', DrugInteractionLookupViewSet)
  
router.register(r'drugCategorys', DrugCategoryViewSet)
router.register(r'drugCategorysWritable', DrugCategoryWritableViewSet)
router.register(r'drugCategorysComplete', DrugCategoryCompleteViewSet)
router.register(r'drugCategorysLookup', DrugCategoryLookupViewSet)

    
