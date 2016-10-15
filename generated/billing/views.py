
from rest_framework import viewsets
from .serializers import *
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class InvoiceLookupViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceLookupSerializer
    
class InvoiceCompleteViewSet(InvoiceViewSet):
    serializer_class = FullInvoiceSerializer
    
class InvoiceWritableViewSet(InvoiceViewSet):
    serializer_class = InvoiceWritableSerializer    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceLookupViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceLookupSerializer
    
class ServiceCompleteViewSet(ServiceViewSet):
    serializer_class = FullServiceSerializer
    
class ServiceWritableViewSet(ServiceViewSet):
    serializer_class = ServiceWritableSerializer    

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    
class InvoiceItemLookupViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemLookupSerializer
    
class InvoiceItemCompleteViewSet(InvoiceItemViewSet):
    serializer_class = FullInvoiceItemSerializer
    
class InvoiceItemWritableViewSet(InvoiceItemViewSet):
    serializer_class = InvoiceItemWritableSerializer    

  