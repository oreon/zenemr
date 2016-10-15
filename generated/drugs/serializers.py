
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction



     
     


     
     
    
class AtcDrugLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = AtcDrug
        fields = ('displayName', 'id',)

class DrugLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Drug
        fields = ('displayName', 'id',)

class DrugInteractionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = DrugInteraction
        fields = ('displayName', 'id',)

class DrugCategoryLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = DrugCategory
        fields = ('displayName', 'id',)
    
    
    
        
    
    

class DrugInteractionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    drug = DrugLookupSerializer()
    interactingDrug = DrugLookupSerializer()
  
    
    class Meta:
        model = DrugInteraction


    
    

class DrugSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    drugInteractions = DrugInteractionSerializer(many=True, read_only = True)
    
    class Meta:
        model = Drug


    
    

class DrugCategorySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = DrugCategory


    
    
        
    
    
    
class DrugInteractionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    drug_displayName = serializers.ReadOnlyField(source='drugDisplayName')
    interactingDrug_displayName = serializers.ReadOnlyField(source='interactingDrugDisplayName')
    
    
    
    drug = serializers.PrimaryKeyRelatedField(queryset=Drug.objects.all())
    
    
    
    
    

    class Meta:
        model = DrugInteraction
        exclude = ('drug',)
    


    
    
    
class DrugWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    drugInteractions = DrugInteractionWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            drugInteractionsCurrent = validated_data.pop('drugInteractions')   
            
            
            drug = Drug.objects.create(**validated_data)
            
            
            for item in drugInteractionsCurrent:
                DrugInteraction(drug=drug, **item).save()    
            
            return drug
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateDrugInteractions(instance, validated_data)    
            
            return super(DrugWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateDrugInteractions(self, instance , validated_data):
        if not 'drugInteractions' in validated_data.keys() : return;
    
        drugInteractionsCurrent = validated_data.pop('drugInteractions')
            
        ids = [item['id'] for item in drugInteractionsCurrent  if 'id' in item.keys() ]
        
        for item in instance.drugInteractions.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in drugInteractionsCurrent:
            DrugInteraction(drug=instance, **item).save()  
     
     

    class Meta:
        model = Drug
        
    


    
    
    
class DrugCategoryWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = DrugCategory
        
    


    
class FullAtcDrugSerializer(AtcDrugSerializer):

 
    
    class Meta(AtcDrugSerializer.Meta):
        model = AtcDrug

class FullDrugSerializer(DrugSerializer):

 
    
    class Meta(DrugSerializer.Meta):
        model = Drug

class FullDrugInteractionSerializer(DrugInteractionSerializer):

 
    
    class Meta(DrugInteractionSerializer.Meta):
        model = DrugInteraction

class FullDrugCategorySerializer(DrugCategorySerializer):

 
    
    class Meta(DrugCategorySerializer.Meta):
        model = DrugCategory

    
  