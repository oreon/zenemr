
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction


     
     
    
class UnusualOccurenceLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = UnusualOccurence
        fields = ('displayName', 'id',)

class OccurenceTypeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = OccurenceType
        fields = ('displayName', 'id',)
    
    
    
    

class UnusualOccurenceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    occurenceType = OccurenceTypeLookupSerializer()
  
    
    class Meta:
        model = UnusualOccurence


    
    

class OccurenceTypeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = OccurenceType


    
    
    
    
class UnusualOccurenceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    occurenceType_displayName = serializers.ReadOnlyField(source='occurenceTypeDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = UnusualOccurence
        
    


    
    
    
class OccurenceTypeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = OccurenceType
        
    


    
class FullUnusualOccurenceSerializer(UnusualOccurenceSerializer):

 
    
    class Meta(UnusualOccurenceSerializer.Meta):
        model = UnusualOccurence

class FullOccurenceTypeSerializer(OccurenceTypeSerializer):

 
    
    class Meta(OccurenceTypeSerializer.Meta):
        model = OccurenceType

    
  