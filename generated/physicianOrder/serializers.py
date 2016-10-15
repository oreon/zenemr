
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     

from  patients.serializers import  PatientLookupSerializer
     
    
class OrderTemplateLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = OrderTemplate
        fields = ('displayName', 'id',)

class OrderLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ('displayName', 'id',)
    
    
    
    

class OrderTemplateSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = OrderTemplate


    
    

class OrderSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    orderTemplate = OrderTemplateLookupSerializer()
    patient = PatientLookupSerializer()
  
    
    class Meta:
        model = Order


    
    
    
    
class OrderTemplateWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = OrderTemplate
        
    


    
    
    
class OrderWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    orderTemplate_displayName = serializers.ReadOnlyField(source='orderTemplateDisplayName')
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Order
        
    


    
class FullOrderTemplateSerializer(OrderTemplateSerializer):

 
    
    class Meta(OrderTemplateSerializer.Meta):
        model = OrderTemplate

class FullOrderSerializer(OrderSerializer):

 
    
    class Meta(OrderSerializer.Meta):
        model = Order

    
  