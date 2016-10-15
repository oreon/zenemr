
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     

     

     
     
    
class SettingsLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Settings
        fields = ('displayName', 'id',)

class SettingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Setting
        fields = ('displayName', 'id',)

class SettingNameLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = SettingName
        fields = ('displayName', 'id',)

class SettingGroupLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = SettingGroup
        fields = ('displayName', 'id',)
    
    
    
    

class SettingsSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Settings


    
    

class SettingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    settingName = SettingNameLookupSerializer()
  
    
    class Meta:
        model = Setting


    
        
    
    

class SettingNameSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    settingGroup = SettingGroupLookupSerializer()
  
    
    class Meta:
        model = SettingName


    
    

class SettingGroupSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    settingNames = SettingNameSerializer(many=True, read_only = True)
    
    class Meta:
        model = SettingGroup


    
    
    
    
class SettingsWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Settings
        
    


    
    
    
class SettingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    settingName_displayName = serializers.ReadOnlyField(source='settingNameDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Setting
        
    


    
        
    
    
    
class SettingNameWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    settingGroup_displayName = serializers.ReadOnlyField(source='settingGroupDisplayName')
    
    
    
    settingGroup = serializers.PrimaryKeyRelatedField(queryset=SettingGroup.objects.all())
    
    
    
    
    

    class Meta:
        model = SettingName
        exclude = ('settingGroup',)
    


    
    
    
class SettingGroupWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    settingNames = SettingNameWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            settingNamesCurrent = validated_data.pop('settingNames')   
            
            
            settingGroup = SettingGroup.objects.create(**validated_data)
            
            
            for item in settingNamesCurrent:
                SettingName(settingGroup=settingGroup, **item).save()    
            
            return settingGroup
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateSettingNames(instance, validated_data)    
            
            return super(SettingGroupWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateSettingNames(self, instance , validated_data):
        if not 'settingNames' in validated_data.keys() : return;
    
        settingNamesCurrent = validated_data.pop('settingNames')
            
        ids = [item['id'] for item in settingNamesCurrent  if 'id' in item.keys() ]
        
        for item in instance.settingNames.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in settingNamesCurrent:
            SettingName(settingGroup=instance, **item).save()  
     
     

    class Meta:
        model = SettingGroup
        
    


    
class FullSettingsSerializer(SettingsSerializer):

 
    
    class Meta(SettingsSerializer.Meta):
        model = Settings

class FullSettingSerializer(SettingSerializer):

 
    
    class Meta(SettingSerializer.Meta):
        model = Setting

class FullSettingNameSerializer(SettingNameSerializer):

 
    
    class Meta(SettingNameSerializer.Meta):
        model = SettingName

class FullSettingGroupSerializer(SettingGroupSerializer):

 
    
    class Meta(SettingGroupSerializer.Meta):
        model = SettingGroup

    
  