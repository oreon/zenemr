
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     


     

     

     
     
    
class FacilityLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Facility
        fields = ('displayName', 'id',)

class RoomLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Room
        fields = ('displayName', 'id',)

class BedLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Bed
        fields = ('displayName', 'id',)

class WardLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Ward
        fields = ('displayName', 'id',)

class RoomTypeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = RoomType
        fields = ('displayName', 'id',)
    
    
    
        
    
        
    
        
    
    

class BedSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    room = RoomLookupSerializer()
  
    
    class Meta:
        model = Bed


    
    

class RoomSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    roomType = RoomTypeLookupSerializer()
    ward = WardLookupSerializer()
  
    beds = BedSerializer(many=True, read_only = True)
    
    class Meta:
        model = Room


    
    

class WardSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    facility = FacilityLookupSerializer()
  
    rooms = RoomSerializer(many=True, read_only = True)
    
    class Meta:
        model = Ward


    
    

class FacilitySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    wards = WardSerializer(many=True, read_only = True)
    
    class Meta:
        model = Facility


    
    

class RoomTypeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = RoomType


    
    
        
    
        
    
        
    
    
    
class BedWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    room_displayName = serializers.ReadOnlyField(source='roomDisplayName')
    
    
    
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    
    
    
    
    

    class Meta:
        model = Bed
        exclude = ('room',)
    


    
    
    
class RoomWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    roomType_displayName = serializers.ReadOnlyField(source='roomTypeDisplayName')
    ward_displayName = serializers.ReadOnlyField(source='wardDisplayName')
    
    
    
    ward = serializers.PrimaryKeyRelatedField(queryset=Ward.objects.all())
    
    
    
    beds = BedWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            bedsCurrent = validated_data.pop('beds')   
            
            
            room = Room.objects.create(**validated_data)
            
            
            for item in bedsCurrent:
                Bed(room=room, **item).save()    
            
            return room
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateBeds(instance, validated_data)    
            
            return super(RoomWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateBeds(self, instance , validated_data):
        if not 'beds' in validated_data.keys() : return;
    
        bedsCurrent = validated_data.pop('beds')
            
        ids = [item['id'] for item in bedsCurrent  if 'id' in item.keys() ]
        
        for item in instance.beds.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in bedsCurrent:
            Bed(room=instance, **item).save()  
     
     

    class Meta:
        model = Room
        exclude = ('ward',)
    


    
    
    
class WardWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    facility_displayName = serializers.ReadOnlyField(source='facilityDisplayName')
    
    
    
    facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
    
    
    
    rooms = RoomWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            roomsCurrent = validated_data.pop('rooms')   
            
            
            ward = Ward.objects.create(**validated_data)
            
            
            for item in roomsCurrent:
                Room(ward=ward, **item).save()    
            
            return ward
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateRooms(instance, validated_data)    
            
            return super(WardWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateRooms(self, instance , validated_data):
        if not 'rooms' in validated_data.keys() : return;
    
        roomsCurrent = validated_data.pop('rooms')
            
        ids = [item['id'] for item in roomsCurrent  if 'id' in item.keys() ]
        
        for item in instance.rooms.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in roomsCurrent:
            Room(ward=instance, **item).save()  
     
     

    class Meta:
        model = Ward
        exclude = ('facility',)
    


    
    
    
class FacilityWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    wards = WardWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            wardsCurrent = validated_data.pop('wards')   
            
            
            facility = Facility.objects.create(**validated_data)
            
            
            for item in wardsCurrent:
                Ward(facility=facility, **item).save()    
            
            return facility
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateWards(instance, validated_data)    
            
            return super(FacilityWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateWards(self, instance , validated_data):
        if not 'wards' in validated_data.keys() : return;
    
        wardsCurrent = validated_data.pop('wards')
            
        ids = [item['id'] for item in wardsCurrent  if 'id' in item.keys() ]
        
        for item in instance.wards.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in wardsCurrent:
            Ward(facility=instance, **item).save()  
     
     

    class Meta:
        model = Facility
        
    


    
    
    
class RoomTypeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = RoomType
        
    


    
class FullFacilitySerializer(FacilitySerializer):

 
    
    class Meta(FacilitySerializer.Meta):
        model = Facility

class FullRoomSerializer(RoomSerializer):

 
    
    class Meta(RoomSerializer.Meta):
        model = Room

class FullBedSerializer(BedSerializer):

 
    
    class Meta(BedSerializer.Meta):
        model = Bed

class FullWardSerializer(WardSerializer):

 
    
    class Meta(WardSerializer.Meta):
        model = Ward

class FullRoomTypeSerializer(RoomTypeSerializer):

 
    
    class Meta(RoomTypeSerializer.Meta):
        model = RoomType

    
  