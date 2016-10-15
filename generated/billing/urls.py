
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicesWritable', InvoiceWritableViewSet)
router.register(r'invoicesComplete', InvoiceCompleteViewSet)
router.register(r'invoicesLookup', InvoiceLookupViewSet)
  
router.register(r'services', ServiceViewSet)
router.register(r'servicesWritable', ServiceWritableViewSet)
router.register(r'servicesComplete', ServiceCompleteViewSet)
router.register(r'servicesLookup', ServiceLookupViewSet)
  
router.register(r'invoiceItems', InvoiceItemViewSet)
router.register(r'invoiceItemsWritable', InvoiceItemWritableViewSet)
router.register(r'invoiceItemsComplete', InvoiceItemCompleteViewSet)
router.register(r'invoiceItemsLookup', InvoiceItemLookupViewSet)

    
