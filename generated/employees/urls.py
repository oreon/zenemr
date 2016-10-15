
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'employees', EmployeeViewSet)
router.register(r'employeesWritable', EmployeeWritableViewSet)
router.register(r'employeesComplete', EmployeeCompleteViewSet)
router.register(r'employeesLookup', EmployeeLookupViewSet)

    
