
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     
     
     


     


     

     


     


     
     
    
class DrugLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Drug
        fields = ('displayName', 'id',)

class CategoryLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('displayName', 'id',)

class PatientLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Patient
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

class EmployeeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ('displayName', 'id',)

class VaccinationLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Vaccination
        fields = ('displayName', 'id',)

class EncounterLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Encounter
        fields = ('displayName', 'id',)

class VaccineLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Vaccine
        fields = ('displayName', 'id',)
    
    
    
    

class DrugSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Drug


    
    

class CategorySerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Category


    
    

class PatientSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Patient


    
        
    
    

class PrescriptionItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    prescription = PrescriptionLookupSerializer()
    drug = DrugLookupSerializer()
  
    
    class Meta:
        model = PrescriptionItem


    
    

class PrescriptionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    encounter = EncounterLookupSerializer()
    patient = PatientLookupSerializer()
  
    prescriptionItems = PrescriptionItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Prescription


    
    

class EmployeeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    #appUser = AppUserLookupSerializer()
  
    class Meta:
        model = Employee


    
    

class VaccinationSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    vaccine = VaccineLookupSerializer()
    patient = PatientLookupSerializer()
  
    
    class Meta:
        model = Vaccination


    
    

class EncounterSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    prescription = PrescriptionLookupSerializer()
    patient = PatientLookupSerializer()
  
    
    class Meta:
        model = Encounter


    
    

class VaccineSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Vaccine


    
    
    
    
class DrugWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Drug
        
    


    
    
    
class CategoryWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Category
        
    


    
    
    
class PatientWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Patient
        
    


    
        
    
    
    
class PrescriptionItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    prescription_displayName = serializers.ReadOnlyField(source='prescriptionDisplayName')
    drug_displayName = serializers.ReadOnlyField(source='drugDisplayName')
    
    
    
    #org.eclipse.uml2.uml.internal.impl.PropertyImpl@5b444398 (name: prescription, visibility: private) (isLeaf: false) (isStatic: false) (isOrdered: false, isUnique: true, isReadOnly: false) (aggregation: none, isDerived: false, isDerivedUnion: false, isID: false) = serializers.PrimaryKeyRelatedField(queryset=Prescription.objects.all())
    
    
    
    
    

    class Meta:
        model = PrescriptionItem
        exclude = ('prescription',)
    


    
    
    
class PrescriptionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    encounter_displayName = serializers.ReadOnlyField(source='encounterDisplayName')
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
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
        
    


    
    
    
class EmployeeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    appUser_displayName = serializers.ReadOnlyField(source='appUserDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Employee
        
    


    
    
    
class VaccinationWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    vaccine_displayName = serializers.ReadOnlyField(source='vaccineDisplayName')
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Vaccination
        
    


    
    
    
class EncounterWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    prescription_displayName = serializers.ReadOnlyField(source='prescriptionDisplayName')
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Encounter
        
    


    
    
    
class VaccineWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Vaccine
        
    


    
class FullDrugSerializer(DrugSerializer):

 
    
    class Meta(DrugSerializer.Meta):
        model = Drug

class FullCategorySerializer(CategorySerializer):

 
    
    class Meta(CategorySerializer.Meta):
        model = Category

class FullPatientSerializer(PatientSerializer):

 
    encounter = EncounterSerializer(many=True, read_only=True)
 
    prescription = PrescriptionSerializer(many=True, read_only=True)
 
    vaccination = VaccinationSerializer(many=True, read_only=True)
 
    
    class Meta(PatientSerializer.Meta):
        model = Patient

class FullPrescriptionSerializer(PrescriptionSerializer):

 
    
    class Meta(PrescriptionSerializer.Meta):
        model = Prescription

class FullPrescriptionItemSerializer(PrescriptionItemSerializer):

 
    
    class Meta(PrescriptionItemSerializer.Meta):
        model = PrescriptionItem

class FullEmployeeSerializer(EmployeeSerializer):

 
    
    class Meta(EmployeeSerializer.Meta):
        model = Employee

class FullVaccinationSerializer(VaccinationSerializer):

 
    
    class Meta(VaccinationSerializer.Meta):
        model = Vaccination

class FullEncounterSerializer(EncounterSerializer):

 
    
    class Meta(EncounterSerializer.Meta):
        model = Encounter

class FullVaccineSerializer(VaccineSerializer):

 
    
    class Meta(VaccineSerializer.Meta):
        model = Vaccine

    
  