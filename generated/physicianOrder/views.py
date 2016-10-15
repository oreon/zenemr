
from rest_framework import viewsets
from .serializers import *
    
class OrderTemplateViewSet(viewsets.ModelViewSet):
    queryset = OrderTemplate.objects.all()
    serializer_class = OrderTemplateSerializer
    
class OrderTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = OrderTemplate.objects.all()
    serializer_class = OrderTemplateLookupSerializer
    
class OrderTemplateCompleteViewSet(OrderTemplateViewSet):
    serializer_class = FullOrderTemplateSerializer
    
class OrderTemplateWritableViewSet(OrderTemplateViewSet):
    serializer_class = OrderTemplateWritableSerializer    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderLookupViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderLookupSerializer
    
class OrderCompleteViewSet(OrderViewSet):
    serializer_class = FullOrderSerializer
    
class OrderWritableViewSet(OrderViewSet):
    serializer_class = OrderWritableSerializer    

  