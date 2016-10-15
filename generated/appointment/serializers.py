
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

from  patients.serializers import  PatientLookupSerializer
from  employees.serializers import  EmployeeLookupSerializer
     
    
class AppointmentLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = ('displayName', 'id',)
    
    
    
    

class AppointmentSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
    employee = EmployeeLookupSerializer()
  
    
    class Meta:
        model = Appointment


    
    
    
    
class AppointmentWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    employee_displayName = serializers.ReadOnlyField(source='employeeDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Appointment
        
    


    
class FullAppointmentSerializer(AppointmentSerializer):

 
    
    class Meta(AppointmentSerializer.Meta):
        model = Appointment

    
  