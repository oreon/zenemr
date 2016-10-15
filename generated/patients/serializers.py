
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     


     

from  prescription.serializers import  PrescriptionLookupSerializer
from  admission.serializers import  AdmissionLookupSerializer
     
     
     


     

     
    
class PatientLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Patient
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

class LabTestLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = LabTest
        fields = ('displayName', 'id',)

class TestResultsLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = TestResults
        fields = ('displayName', 'id',)

class ResultRowLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ResultRow
        fields = ('displayName', 'id',)
    
    
    
    

class PatientSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Patient


    
    

class VaccinationSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    vaccine = VaccineLookupSerializer()
    patient = PatientLookupSerializer()
  
    
    class Meta:
        model = Vaccination


    
    

class EncounterSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
    prescription = PrescriptionLookupSerializer()
    admission = AdmissionLookupSerializer()
  
    
    class Meta:
        model = Encounter


    
    

class VaccineSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Vaccine


    
    

class LabTestSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = LabTest


    
        
    
    

class ResultRowSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    testResults = TestResultsLookupSerializer()
  
    
    class Meta:
        model = ResultRow


    
    

class TestResultsSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
    labTest = LabTestLookupSerializer()
  
    resultRows = ResultRowSerializer(many=True, read_only = True)
    
    class Meta:
        model = TestResults


    
    
    
    
class PatientWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Patient
        
    


    
    
    
class VaccinationWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    vaccine_displayName = serializers.ReadOnlyField(source='vaccineDisplayName')
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Vaccination
        
    


    
    
    
class EncounterWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    prescription_displayName = serializers.ReadOnlyField(source='prescriptionDisplayName')
    admission_displayName = serializers.ReadOnlyField(source='admissionDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Encounter
        
    


    
    
    
class VaccineWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Vaccine
        
    


    
    
    
class LabTestWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = LabTest
        
    


    
        
    
    
    
class ResultRowWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    testResults_displayName = serializers.ReadOnlyField(source='testResultsDisplayName')
    
    
    
    testResults = serializers.PrimaryKeyRelatedField(queryset=TestResults.objects.all())
    
    
    
    
    

    class Meta:
        model = ResultRow
        exclude = ('testResults',)
    


    
    
    
class TestResultsWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    labTest_displayName = serializers.ReadOnlyField(source='labTestDisplayName')
    
    
    
    
    
    resultRows = ResultRowWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            resultRowsCurrent = validated_data.pop('resultRows')   
            
            
            testResults = TestResults.objects.create(**validated_data)
            
            
            for item in resultRowsCurrent:
                ResultRow(testResults=testResults, **item).save()    
            
            return testResults
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateResultRows(instance, validated_data)    
            
            return super(TestResultsWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateResultRows(self, instance , validated_data):
        if not 'resultRows' in validated_data.keys() : return;
    
        resultRowsCurrent = validated_data.pop('resultRows')
            
        ids = [item['id'] for item in resultRowsCurrent  if 'id' in item.keys() ]
        
        for item in instance.resultRows.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in resultRowsCurrent:
            ResultRow(testResults=instance, **item).save()  
     
     

    class Meta:
        model = TestResults
        
    


    
class FullPatientSerializer(PatientSerializer):

 
    encounter = EncounterSerializer(many=True, read_only=True)
 
    vaccination = VaccinationSerializer(many=True, read_only=True)
 
    testResults = TestResultsSerializer(many=True, read_only=True)
 
    
    class Meta(PatientSerializer.Meta):
        model = Patient

class FullVaccinationSerializer(VaccinationSerializer):

 
    
    class Meta(VaccinationSerializer.Meta):
        model = Vaccination

class FullEncounterSerializer(EncounterSerializer):

 
    
    class Meta(EncounterSerializer.Meta):
        model = Encounter

class FullVaccineSerializer(VaccineSerializer):

 
    
    class Meta(VaccineSerializer.Meta):
        model = Vaccine

class FullLabTestSerializer(LabTestSerializer):

 
    
    class Meta(LabTestSerializer.Meta):
        model = LabTest

class FullTestResultsSerializer(TestResultsSerializer):

 
    
    class Meta(TestResultsSerializer.Meta):
        model = TestResults

class FullResultRowSerializer(ResultRowSerializer):

 
    
    class Meta(ResultRowSerializer.Meta):
        model = ResultRow

    
  