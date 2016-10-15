
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     
     
     


     

     
     


     
     


     
     
     
     
    
class FindingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Finding
        fields = ('displayName', 'id',)

class PhysicalFindingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PhysicalFinding
        fields = ('displayName', 'id',)

class LabFindingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = LabFinding
        fields = ('displayName', 'id',)

class DiseaseLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Disease
        fields = ('displayName', 'id',)

class ConditionFindingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ConditionFinding
        fields = ('displayName', 'id',)

class ConditionCategoryLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ConditionCategory
        fields = ('displayName', 'id',)

class DifferentialDxLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = DifferentialDx
        fields = ('displayName', 'id',)

class DxCategoryLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = DxCategory
        fields = ('displayName', 'id',)

class PatientFindingLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PatientFinding
        fields = ('displayName', 'id',)

class PatientDiffDxLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = PatientDiffDx
        fields = ('displayName', 'id',)

class DxTestLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = DxTest
        fields = ('displayName', 'id',)

class ChronicConditionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ChronicCondition
        fields = ('displayName', 'id',)
    
    
    
        
    
    

class DifferentialDxSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    dxCategory = DxCategoryLookupSerializer()
    finding = FindingLookupSerializer()
  
    
    class Meta:
        model = DifferentialDx


    
    

class FindingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    differentialDxs = DifferentialDxSerializer(many=True, read_only = True)
    
    class Meta:
        model = Finding


    
        
    
    

class DifferentialDxSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    dxCategory = DxCategoryLookupSerializer()
    finding = FindingLookupSerializer()
  
    
    class Meta:
        model = DifferentialDx


    
    

class PhysicalFindingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    differentialDxs = DifferentialDxSerializer(many=True, read_only = True)
    
    class Meta:
        model = PhysicalFinding


    
        
    
    

class DifferentialDxSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    dxCategory = DxCategoryLookupSerializer()
    finding = FindingLookupSerializer()
  
    
    class Meta:
        model = DifferentialDx


    
    

class LabFindingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    differentialDxs = DifferentialDxSerializer(many=True, read_only = True)
    
    class Meta:
        model = LabFinding


    
    

class DiseaseSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    relatedDisease = DiseaseLookupSerializer()
    conditionCategory = ConditionCategoryLookupSerializer()
  
    
    class Meta:
        model = Disease


    
    

class ConditionFindingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    disease = DiseaseLookupSerializer()
  
    
    class Meta:
        model = ConditionFinding


    
    

class ConditionCategorySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = ConditionCategory


    
    

class DxCategorySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = DxCategory


    
        
    
    

class PatientFindingSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    finding = FindingLookupSerializer()
    patientDiffDx = PatientDiffDxLookupSerializer()
  
    
    class Meta:
        model = PatientFinding


    
    

class PatientDiffDxSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    patientFindings = PatientFindingSerializer(many=True, read_only = True)
    
    class Meta:
        model = PatientDiffDx


    
    

class DxTestSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = DxTest


    
    

class ChronicConditionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = ChronicCondition


    
    
        
    
    
    
class DifferentialDxWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    dxCategory_displayName = serializers.ReadOnlyField(source='dxCategoryDisplayName')
    finding_displayName = serializers.ReadOnlyField(source='findingDisplayName')
    
    
    
    finding = serializers.PrimaryKeyRelatedField(queryset=Finding.objects.all())
    
    
    
    
    

    class Meta:
        model = DifferentialDx
        exclude = ('finding',)
    


    
    
    
class FindingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    differentialDxs = DifferentialDxWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            differentialDxsCurrent = validated_data.pop('differentialDxs')   
            
            
            finding = Finding.objects.create(**validated_data)
            
            
            for item in differentialDxsCurrent:
                DifferentialDx(finding=finding, **item).save()    
            
            return finding
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateDifferentialDxs(instance, validated_data)    
            
            return super(FindingWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateDifferentialDxs(self, instance , validated_data):
        if not 'differentialDxs' in validated_data.keys() : return;
    
        differentialDxsCurrent = validated_data.pop('differentialDxs')
            
        ids = [item['id'] for item in differentialDxsCurrent  if 'id' in item.keys() ]
        
        for item in instance.differentialDxs.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in differentialDxsCurrent:
            DifferentialDx(finding=instance, **item).save()  
     
     

    class Meta:
        model = Finding
        
    


    
        
    
    
    
class DifferentialDxWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    dxCategory_displayName = serializers.ReadOnlyField(source='dxCategoryDisplayName')
    finding_displayName = serializers.ReadOnlyField(source='findingDisplayName')
    
    
    
    finding = serializers.PrimaryKeyRelatedField(queryset=Finding.objects.all())
    
    
    
    
    

    class Meta:
        model = DifferentialDx
        exclude = ('finding',)
    


    
    
    
class PhysicalFindingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    differentialDxs = DifferentialDxWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            differentialDxsCurrent = validated_data.pop('differentialDxs')   
            
            
            physicalFinding = PhysicalFinding.objects.create(**validated_data)
            
            
            for item in differentialDxsCurrent:
                DifferentialDx(physicalFinding=physicalFinding, **item).save()    
            
            return physicalFinding
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateDifferentialDxs(instance, validated_data)    
            
            return super(PhysicalFindingWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateDifferentialDxs(self, instance , validated_data):
        if not 'differentialDxs' in validated_data.keys() : return;
    
        differentialDxsCurrent = validated_data.pop('differentialDxs')
            
        ids = [item['id'] for item in differentialDxsCurrent  if 'id' in item.keys() ]
        
        for item in instance.differentialDxs.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in differentialDxsCurrent:
            DifferentialDx(physicalFinding=instance, **item).save()  
     
     

    class Meta:
        model = PhysicalFinding
        
    


    
        
    
    
    
class DifferentialDxWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    dxCategory_displayName = serializers.ReadOnlyField(source='dxCategoryDisplayName')
    finding_displayName = serializers.ReadOnlyField(source='findingDisplayName')
    
    
    
    finding = serializers.PrimaryKeyRelatedField(queryset=Finding.objects.all())
    
    
    
    
    

    class Meta:
        model = DifferentialDx
        exclude = ('finding',)
    


    
    
    
class LabFindingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    differentialDxs = DifferentialDxWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            differentialDxsCurrent = validated_data.pop('differentialDxs')   
            
            
            labFinding = LabFinding.objects.create(**validated_data)
            
            
            for item in differentialDxsCurrent:
                DifferentialDx(labFinding=labFinding, **item).save()    
            
            return labFinding
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateDifferentialDxs(instance, validated_data)    
            
            return super(LabFindingWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateDifferentialDxs(self, instance , validated_data):
        if not 'differentialDxs' in validated_data.keys() : return;
    
        differentialDxsCurrent = validated_data.pop('differentialDxs')
            
        ids = [item['id'] for item in differentialDxsCurrent  if 'id' in item.keys() ]
        
        for item in instance.differentialDxs.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in differentialDxsCurrent:
            DifferentialDx(labFinding=instance, **item).save()  
     
     

    class Meta:
        model = LabFinding
        
    


    
    
    
class DiseaseWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    relatedDisease_displayName = serializers.ReadOnlyField(source='relatedDiseaseDisplayName')
    conditionCategory_displayName = serializers.ReadOnlyField(source='conditionCategoryDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Disease
        
    


    
    
    
class ConditionFindingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    disease_displayName = serializers.ReadOnlyField(source='diseaseDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = ConditionFinding
        
    


    
    
    
class ConditionCategoryWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = ConditionCategory
        
    


    
    
    
class DxCategoryWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = DxCategory
        
    


    
        
    
    
    
class PatientFindingWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    finding_displayName = serializers.ReadOnlyField(source='findingDisplayName')
    patientDiffDx_displayName = serializers.ReadOnlyField(source='patientDiffDxDisplayName')
    
    
    
    patientDiffDx = serializers.PrimaryKeyRelatedField(queryset=PatientDiffDx.objects.all())
    
    
    
    
    

    class Meta:
        model = PatientFinding
        exclude = ('patientDiffDx',)
    


    
    
    
class PatientDiffDxWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    patientFindings = PatientFindingWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            patientFindingsCurrent = validated_data.pop('patientFindings')   
            
            
            patientDiffDx = PatientDiffDx.objects.create(**validated_data)
            
            
            for item in patientFindingsCurrent:
                PatientFinding(patientDiffDx=patientDiffDx, **item).save()    
            
            return patientDiffDx
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updatePatientFindings(instance, validated_data)    
            
            return super(PatientDiffDxWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updatePatientFindings(self, instance , validated_data):
        if not 'patientFindings' in validated_data.keys() : return;
    
        patientFindingsCurrent = validated_data.pop('patientFindings')
            
        ids = [item['id'] for item in patientFindingsCurrent  if 'id' in item.keys() ]
        
        for item in instance.patientFindings.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in patientFindingsCurrent:
            PatientFinding(patientDiffDx=instance, **item).save()  
     
     

    class Meta:
        model = PatientDiffDx
        
    


    
    
    
class DxTestWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = DxTest
        
    


    
    
    
class ChronicConditionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = ChronicCondition
        
    


    
class FullFindingSerializer(FindingSerializer):

 
    
    class Meta(FindingSerializer.Meta):
        model = Finding

class FullPhysicalFindingSerializer(PhysicalFindingSerializer):

 
    
    class Meta(PhysicalFindingSerializer.Meta):
        model = PhysicalFinding

class FullLabFindingSerializer(LabFindingSerializer):

 
    
    class Meta(LabFindingSerializer.Meta):
        model = LabFinding

class FullDiseaseSerializer(DiseaseSerializer):

 
    differentialDiagnoses = DiseaseSerializer(many=True, read_only=True)
 
    
    class Meta(DiseaseSerializer.Meta):
        model = Disease

class FullConditionFindingSerializer(ConditionFindingSerializer):

 
    
    class Meta(ConditionFindingSerializer.Meta):
        model = ConditionFinding

class FullConditionCategorySerializer(ConditionCategorySerializer):

 
    
    class Meta(ConditionCategorySerializer.Meta):
        model = ConditionCategory

class FullDifferentialDxSerializer(DifferentialDxSerializer):

 
    
    class Meta(DifferentialDxSerializer.Meta):
        model = DifferentialDx

class FullDxCategorySerializer(DxCategorySerializer):

 
    
    class Meta(DxCategorySerializer.Meta):
        model = DxCategory

class FullPatientFindingSerializer(PatientFindingSerializer):

 
    
    class Meta(PatientFindingSerializer.Meta):
        model = PatientFinding

class FullPatientDiffDxSerializer(PatientDiffDxSerializer):

 
    
    class Meta(PatientDiffDxSerializer.Meta):
        model = PatientDiffDx

class FullDxTestSerializer(DxTestSerializer):

 
    
    class Meta(DxTestSerializer.Meta):
        model = DxTest

class FullChronicConditionSerializer(ChronicConditionSerializer):

 
    charts = ChartSerializer(many=True, read_only=True)
 
    
    class Meta(ChronicConditionSerializer.Meta):
        model = ChronicCondition

    
  