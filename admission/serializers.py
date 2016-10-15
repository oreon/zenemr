
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

from  billing.serializers import  InvoiceLookupSerializer
     

     
    
class AdmissionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Admission
        fields = ('displayName', 'id',)

class BedStayLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = BedStay
        fields = ('displayName', 'id',)
    
    
    
        
    
    

class BedStaySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    admission = AdmissionLookupSerializer()
  
    
    class Meta:
        model = BedStay


    
    

class AdmissionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    invoice = InvoiceLookupSerializer()
  
    bedStays = BedStaySerializer(many=True, read_only = True)
    
    class Meta:
        model = Admission


    
    
        
    
    
    
class BedStayWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    admission_displayName = serializers.ReadOnlyField(source='admissionDisplayName')
    
    
    
    admission = serializers.PrimaryKeyRelatedField(queryset=Admission.objects.all())
    
    
    
    
    

    class Meta:
        model = BedStay
        exclude = ('admission',)
    


    
    
    
class AdmissionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    invoice_displayName = serializers.ReadOnlyField(source='invoiceDisplayName')
    
    
    
    
    
    bedStays = BedStayWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            bedStaysCurrent = validated_data.pop('bedStays')   
            
            
            admission = Admission.objects.create(**validated_data)
            
            
            for item in bedStaysCurrent:
                BedStay(admission=admission, **item).save()    
            
            return admission
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateBedStays(instance, validated_data)    
            
            return super(AdmissionWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateBedStays(self, instance , validated_data):
        if not 'bedStays' in validated_data.keys() : return;
    
        bedStaysCurrent = validated_data.pop('bedStays')
            
        ids = [item['id'] for item in bedStaysCurrent  if 'id' in item.keys() ]
        
        for item in instance.bedStays.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in bedStaysCurrent:
            BedStay(admission=instance, **item).save()  
     
     

    class Meta:
        model = Admission
        
    


    
class FullAdmissionSerializer(AdmissionSerializer):

 
    encounter = EncounterSerializer(many=True, read_only=True)
 
    
    class Meta(AdmissionSerializer.Meta):
        model = Admission

class FullBedStaySerializer(BedStaySerializer):

 
    
    class Meta(BedStaySerializer.Meta):
        model = BedStay

    
  