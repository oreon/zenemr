
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

from  users.serializers import  AppUserLookupSerializer
     
    
class EmployeeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ('displayName', 'id',)
    
    
    
    

class EmployeeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    appUser = AppUserLookupSerializer()
  
    
    class Meta:
        model = Employee


    
    
    
    
class EmployeeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    appUser_displayName = serializers.ReadOnlyField(source='appUserDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Employee
        
    


    
class FullEmployeeSerializer(EmployeeSerializer):

 
    
    class Meta(EmployeeSerializer.Meta):
        model = Employee

    
  