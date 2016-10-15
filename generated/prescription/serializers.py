
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     
from  patients.serializers import  EncounterLookupSerializer
     
from  drugs.serializers import  DrugLookupSerializer


     
from  drugs.serializers import  DrugLookupSerializer


     
     
    
class PrescriptionTemplateLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PrescriptionTemplate
        fields = ('displayName', 'id',)

class PrescriptionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Prescription
        fields = ('displayName', 'id',)

class PrescriptionItemLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PrescriptionItem
        fields = ('displayName', 'id',)

class PrescriptionItemTemplateLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PrescriptionItemTemplate
        fields = ('displayName', 'id',)

class FrequencyLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Frequency
        fields = ('displayName', 'id',)
    
    
    
        
    
    

class PrescriptionItemTemplateSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    drug = DrugLookupSerializer()
    frequency = FrequencyLookupSerializer()
    prescriptionTemplate = PrescriptionTemplateLookupSerializer()
  
    
    class Meta:
        model = PrescriptionItemTemplate


    
    

class PrescriptionTemplateSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    prescriptionItemTemplates = PrescriptionItemTemplateSerializer(many=True, read_only = True)
    
    class Meta:
        model = PrescriptionTemplate


    
        
    
    

class PrescriptionItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    drug = DrugLookupSerializer()
    prescription = PrescriptionLookupSerializer()
    frequency = FrequencyLookupSerializer()
  
    
    class Meta:
        model = PrescriptionItem


    
    

class PrescriptionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    encounter = EncounterLookupSerializer()
  
    prescriptionItems = PrescriptionItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Prescription


    
    

class FrequencySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Frequency


    
    
        
    
    
    
class PrescriptionItemTemplateWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    drug_displayName = serializers.ReadOnlyField(source='drugDisplayName')
    frequency_displayName = serializers.ReadOnlyField(source='frequencyDisplayName')
    prescriptionTemplate_displayName = serializers.ReadOnlyField(source='prescriptionTemplateDisplayName')
    
    
    
    prescriptionTemplate = serializers.PrimaryKeyRelatedField(queryset=PrescriptionTemplate.objects.all())
    
    
    
    
    

    class Meta:
        model = PrescriptionItemTemplate
        exclude = ('prescriptionTemplate',)
    


    
    
    
class PrescriptionTemplateWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    prescriptionItemTemplates = PrescriptionItemTemplateWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            prescriptionItemTemplatesCurrent = validated_data.pop('prescriptionItemTemplates')   
            
            
            prescriptionTemplate = PrescriptionTemplate.objects.create(**validated_data)
            
            
            for item in prescriptionItemTemplatesCurrent:
                PrescriptionItemTemplate(prescriptionTemplate=prescriptionTemplate, **item).save()    
            
            return prescriptionTemplate
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updatePrescriptionItemTemplates(instance, validated_data)    
            
            return super(PrescriptionTemplateWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updatePrescriptionItemTemplates(self, instance , validated_data):
        if not 'prescriptionItemTemplates' in validated_data.keys() : return;
    
        prescriptionItemTemplatesCurrent = validated_data.pop('prescriptionItemTemplates')
            
        ids = [item['id'] for item in prescriptionItemTemplatesCurrent  if 'id' in item.keys() ]
        
        for item in instance.prescriptionItemTemplates.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in prescriptionItemTemplatesCurrent:
            PrescriptionItemTemplate(prescriptionTemplate=instance, **item).save()  
     
     

    class Meta:
        model = PrescriptionTemplate
        
    


    
        
    
    
    
class PrescriptionItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    drug_displayName = serializers.ReadOnlyField(source='drugDisplayName')
    prescription_displayName = serializers.ReadOnlyField(source='prescriptionDisplayName')
    frequency_displayName = serializers.ReadOnlyField(source='frequencyDisplayName')
    
    
    
    prescription = serializers.PrimaryKeyRelatedField(queryset=Prescription.objects.all())
    
    
    
    
    

    class Meta:
        model = PrescriptionItem
        exclude = ('prescription',)
    


    
    
    
class PrescriptionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    encounter_displayName = serializers.ReadOnlyField(source='encounterDisplayName')
    
    
    
    
    
    prescriptionItems = PrescriptionItemWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            prescriptionItemsCurrent = validated_data.pop('prescriptionItems')   
            
            
            prescription = Prescription.objects.create(**validated_data)
            
            
            for item in prescriptionItemsCurrent:
                PrescriptionItem(prescription=prescription, **item).save()    
            
            return prescription
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updatePrescriptionItems(instance, validated_data)    
            
            return super(PrescriptionWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updatePrescriptionItems(self, instance , validated_data):
        if not 'prescriptionItems' in validated_data.keys() : return;
    
        prescriptionItemsCurrent = validated_data.pop('prescriptionItems')
            
        ids = [item['id'] for item in prescriptionItemsCurrent  if 'id' in item.keys() ]
        
        for item in instance.prescriptionItems.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in prescriptionItemsCurrent:
            PrescriptionItem(prescription=instance, **item).save()  
     
     

    class Meta:
        model = Prescription
        
    


    
    
    
class FrequencyWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Frequency
        
    


    
class FullPrescriptionTemplateSerializer(PrescriptionTemplateSerializer):

 
    
    class Meta(PrescriptionTemplateSerializer.Meta):
        model = PrescriptionTemplate

class FullPrescriptionSerializer(PrescriptionSerializer):

 
    
    class Meta(PrescriptionSerializer.Meta):
        model = Prescription

class FullPrescriptionItemSerializer(PrescriptionItemSerializer):

 
    
    class Meta(PrescriptionItemSerializer.Meta):
        model = PrescriptionItem

class FullPrescriptionItemTemplateSerializer(PrescriptionItemTemplateSerializer):

 
    
    class Meta(PrescriptionItemTemplateSerializer.Meta):
        model = PrescriptionItemTemplate

class FullFrequencySerializer(FrequencySerializer):

 
    
    class Meta(FrequencySerializer.Meta):
        model = Frequency

    
  