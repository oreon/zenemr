
from rest_framework import viewsets
from .serializers import *
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeLookupViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeLookupSerializer
    
class EmployeeCompleteViewSet(EmployeeViewSet):
    serializer_class = FullEmployeeSerializer
    
class EmployeeWritableViewSet(EmployeeViewSet):
    serializer_class = EmployeeWritableSerializer    

  