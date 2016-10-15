
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'orderTemplates', OrderTemplateViewSet)
router.register(r'orderTemplatesWritable', OrderTemplateWritableViewSet)
router.register(r'orderTemplatesComplete', OrderTemplateCompleteViewSet)
router.register(r'orderTemplatesLookup', OrderTemplateLookupViewSet)
  
router.register(r'orders', OrderViewSet)
router.register(r'ordersWritable', OrderWritableViewSet)
router.register(r'ordersComplete', OrderCompleteViewSet)
router.register(r'ordersLookup', OrderLookupViewSet)

    
