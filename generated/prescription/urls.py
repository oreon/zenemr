
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'prescriptionTemplates', PrescriptionTemplateViewSet)
router.register(r'prescriptionTemplatesWritable', PrescriptionTemplateWritableViewSet)
router.register(r'prescriptionTemplatesComplete', PrescriptionTemplateCompleteViewSet)
router.register(r'prescriptionTemplatesLookup', PrescriptionTemplateLookupViewSet)
  
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'prescriptionsWritable', PrescriptionWritableViewSet)
router.register(r'prescriptionsComplete', PrescriptionCompleteViewSet)
router.register(r'prescriptionsLookup', PrescriptionLookupViewSet)
  
router.register(r'prescriptionItems', PrescriptionItemViewSet)
router.register(r'prescriptionItemsWritable', PrescriptionItemWritableViewSet)
router.register(r'prescriptionItemsComplete', PrescriptionItemCompleteViewSet)
router.register(r'prescriptionItemsLookup', PrescriptionItemLookupViewSet)
  
router.register(r'prescriptionItemTemplates', PrescriptionItemTemplateViewSet)
router.register(r'prescriptionItemTemplatesWritable', PrescriptionItemTemplateWritableViewSet)
router.register(r'prescriptionItemTemplatesComplete', PrescriptionItemTemplateCompleteViewSet)
router.register(r'prescriptionItemTemplatesLookup', PrescriptionItemTemplateLookupViewSet)
  
router.register(r'frequencys', FrequencyViewSet)
router.register(r'frequencysWritable', FrequencyWritableViewSet)
router.register(r'frequencysComplete', FrequencyCompleteViewSet)
router.register(r'frequencysLookup', FrequencyLookupViewSet)

    
