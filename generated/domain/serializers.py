
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

     
     
     
     


     

from  prescription.serializers import  PrescriptionLookupSerializer
from  admission.serializers import  AdmissionLookupSerializer
     
     
     


     

     
     


     

     

     
     

     
     
     

     

     
     
     
from  patients.serializers import  EncounterLookupSerializer
     
from  drugs.serializers import  DrugLookupSerializer


     
from  drugs.serializers import  DrugLookupSerializer


     
     


     
     


     
     
     
     
     


     

     
     


     
     


     
     
     
     

     
     

     
     

     
from  ddx.serializers import  ChronicConditionLookupSerializer
     

     

     
from  patients.serializers import  PatientLookupSerializer
     
     


     
from  patients.serializers import  PatientLookupSerializer
from  employees.serializers import  EmployeeLookupSerializer
     
from  billing.serializers import  InvoiceLookupSerializer
     

     
from  users.serializers import  AppUserLookupSerializer
     
     

from  patients.serializers import  PatientLookupSerializer
     
    
class AppUserLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = AppUser
        fields = ('displayName', 'id',)

class AppRoleLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = AppRole
        fields = ('displayName', 'id',)

class GroupLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Group
        fields = ('displayName', 'id',)

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

class CodeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Code
        fields = ('displayName', 'id',)

class ChapterLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Chapter
        fields = ('displayName', 'id',)

class SectionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Section
        fields = ('displayName', 'id',)

class SimpleCodeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = SimpleCode
        fields = ('displayName', 'id',)

class AppliedChartLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = AppliedChart
        fields = ('displayName', 'id',)

class ChartLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Chart
        fields = ('displayName', 'id',)

class ChartItemLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ChartItem
        fields = ('displayName', 'id',)

class ChartProcedureLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ChartProcedure
        fields = ('displayName', 'id',)

class InvoiceLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = ('displayName', 'id',)

class ServiceLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = ('displayName', 'id',)

class InvoiceItemLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = InvoiceItem
        fields = ('displayName', 'id',)

class AppointmentLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = ('displayName', 'id',)

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

class EmployeeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ('displayName', 'id',)

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
    
    
    
    

class AppUserSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = AppUser


    
    

class AppRoleSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = AppRole


    
    

class GroupSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Group


    
    

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


    
    

class UnusualOccurenceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    occurenceType = OccurenceTypeLookupSerializer()
  
    
    class Meta:
        model = UnusualOccurence


    
    

class OccurenceTypeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = OccurenceType


    
    

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


    
        
    
        
    
    

class CodeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    section = SectionLookupSerializer()
  
    
    class Meta:
        model = Code


    
    

class SectionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chapter = ChapterLookupSerializer()
  
    codes = CodeSerializer(many=True, read_only = True)
    
    class Meta:
        model = Section


    
    

class ChapterSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    sections = SectionSerializer(many=True, read_only = True)
    
    class Meta:
        model = Chapter


    
    

class SimpleCodeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = SimpleCode


    
    

class AppliedChartSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chart = ChartLookupSerializer()
  
    
    class Meta:
        model = AppliedChart


    
        
    
    

class ChartItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chart = ChartLookupSerializer()
  
    
    class Meta:
        model = ChartItem


    
    

class ChartSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chronicCondition = ChronicConditionLookupSerializer()
  
    chartItems = ChartItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Chart


    
    

class ChartProcedureSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chartItem = ChartItemLookupSerializer()
  
    
    class Meta:
        model = ChartProcedure


    
        
    
    

class InvoiceItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    service = ServiceLookupSerializer()
    invoice = InvoiceLookupSerializer()
  
    
    class Meta:
        model = InvoiceItem


    
    

class InvoiceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
  
    invoiceItems = InvoiceItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Invoice


    
    

class ServiceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Service


    
    

class AppointmentSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
    employee = EmployeeLookupSerializer()
  
    
    class Meta:
        model = Appointment


    
        
    
    

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


    
    

class EmployeeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    appUser = AppUserLookupSerializer()
  
    
    class Meta:
        model = Employee


    
    

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


    
    
    
    
class AppUserWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = AppUser
        
    


    
    
    
class AppRoleWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = AppRole
        
    


    
    
    
class GroupWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Group
        
    


    
    
    
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
        
    


    
    
    
class UnusualOccurenceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    occurenceType_displayName = serializers.ReadOnlyField(source='occurenceTypeDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = UnusualOccurence
        
    


    
    
    
class OccurenceTypeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = OccurenceType
        
    


    
    
    
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
        
    


    
        
    
        
    
    
    
class CodeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    section_displayName = serializers.ReadOnlyField(source='sectionDisplayName')
    
    
    
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())
    
    
    
    
    

    class Meta:
        model = Code
        exclude = ('section',)
    


    
    
    
class SectionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chapter_displayName = serializers.ReadOnlyField(source='chapterDisplayName')
    
    
    
    chapter = serializers.PrimaryKeyRelatedField(queryset=Chapter.objects.all())
    
    
    
    codes = CodeWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            codesCurrent = validated_data.pop('codes')   
            
            
            section = Section.objects.create(**validated_data)
            
            
            for item in codesCurrent:
                Code(section=section, **item).save()    
            
            return section
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateCodes(instance, validated_data)    
            
            return super(SectionWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateCodes(self, instance , validated_data):
        if not 'codes' in validated_data.keys() : return;
    
        codesCurrent = validated_data.pop('codes')
            
        ids = [item['id'] for item in codesCurrent  if 'id' in item.keys() ]
        
        for item in instance.codes.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in codesCurrent:
            Code(section=instance, **item).save()  
     
     

    class Meta:
        model = Section
        exclude = ('chapter',)
    


    
    
    
class ChapterWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    sections = SectionWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            sectionsCurrent = validated_data.pop('sections')   
            
            
            chapter = Chapter.objects.create(**validated_data)
            
            
            for item in sectionsCurrent:
                Section(chapter=chapter, **item).save()    
            
            return chapter
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateSections(instance, validated_data)    
            
            return super(ChapterWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateSections(self, instance , validated_data):
        if not 'sections' in validated_data.keys() : return;
    
        sectionsCurrent = validated_data.pop('sections')
            
        ids = [item['id'] for item in sectionsCurrent  if 'id' in item.keys() ]
        
        for item in instance.sections.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in sectionsCurrent:
            Section(chapter=instance, **item).save()  
     
     

    class Meta:
        model = Chapter
        
    


    
    
    
class SimpleCodeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = SimpleCode
        
    


    
    
    
class AppliedChartWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chart_displayName = serializers.ReadOnlyField(source='chartDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = AppliedChart
        
    


    
        
    
    
    
class ChartItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chart_displayName = serializers.ReadOnlyField(source='chartDisplayName')
    
    
    
    chart = serializers.PrimaryKeyRelatedField(queryset=Chart.objects.all())
    
    
    
    
    

    class Meta:
        model = ChartItem
        exclude = ('chart',)
    


    
    
    
class ChartWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chronicCondition_displayName = serializers.ReadOnlyField(source='chronicConditionDisplayName')
    
    
    
    
    
    chartItems = ChartItemWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            chartItemsCurrent = validated_data.pop('chartItems')   
            
            
            chart = Chart.objects.create(**validated_data)
            
            
            for item in chartItemsCurrent:
                ChartItem(chart=chart, **item).save()    
            
            return chart
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateChartItems(instance, validated_data)    
            
            return super(ChartWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateChartItems(self, instance , validated_data):
        if not 'chartItems' in validated_data.keys() : return;
    
        chartItemsCurrent = validated_data.pop('chartItems')
            
        ids = [item['id'] for item in chartItemsCurrent  if 'id' in item.keys() ]
        
        for item in instance.chartItems.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in chartItemsCurrent:
            ChartItem(chart=instance, **item).save()  
     
     

    class Meta:
        model = Chart
        
    


    
    
    
class ChartProcedureWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chartItem_displayName = serializers.ReadOnlyField(source='chartItemDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = ChartProcedure
        
    


    
        
    
    
    
class InvoiceItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    service_displayName = serializers.ReadOnlyField(source='serviceDisplayName')
    invoice_displayName = serializers.ReadOnlyField(source='invoiceDisplayName')
    
    
    
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    
    
    
    
    

    class Meta:
        model = InvoiceItem
        exclude = ('invoice',)
    


    
    
    
class InvoiceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    invoiceItems = InvoiceItemWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            invoiceItemsCurrent = validated_data.pop('invoiceItems')   
            
            
            invoice = Invoice.objects.create(**validated_data)
            
            
            for item in invoiceItemsCurrent:
                InvoiceItem(invoice=invoice, **item).save()    
            
            return invoice
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateInvoiceItems(instance, validated_data)    
            
            return super(InvoiceWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateInvoiceItems(self, instance , validated_data):
        if not 'invoiceItems' in validated_data.keys() : return;
    
        invoiceItemsCurrent = validated_data.pop('invoiceItems')
            
        ids = [item['id'] for item in invoiceItemsCurrent  if 'id' in item.keys() ]
        
        for item in instance.invoiceItems.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in invoiceItemsCurrent:
            InvoiceItem(invoice=instance, **item).save()  
     
     

    class Meta:
        model = Invoice
        
    


    
    
    
class ServiceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Service
        
    


    
    
    
class AppointmentWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    employee_displayName = serializers.ReadOnlyField(source='employeeDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Appointment
        
    


    
        
    
    
    
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
        
    


    
    
    
class EmployeeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    appUser_displayName = serializers.ReadOnlyField(source='appUserDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = Employee
        
    


    
    
    
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
        
    


    
class FullAppUserSerializer(AppUserSerializer):

 
    
    class Meta(AppUserSerializer.Meta):
        model = AppUser

class FullAppRoleSerializer(AppRoleSerializer):

 
    
    class Meta(AppRoleSerializer.Meta):
        model = AppRole

class FullGroupSerializer(GroupSerializer):

 
    
    class Meta(GroupSerializer.Meta):
        model = Group

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

class FullUnusualOccurenceSerializer(UnusualOccurenceSerializer):

 
    
    class Meta(UnusualOccurenceSerializer.Meta):
        model = UnusualOccurence

class FullOccurenceTypeSerializer(OccurenceTypeSerializer):

 
    
    class Meta(OccurenceTypeSerializer.Meta):
        model = OccurenceType

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

class FullCodeSerializer(CodeSerializer):

 
    
    class Meta(CodeSerializer.Meta):
        model = Code

class FullChapterSerializer(ChapterSerializer):

 
    
    class Meta(ChapterSerializer.Meta):
        model = Chapter

class FullSectionSerializer(SectionSerializer):

 
    
    class Meta(SectionSerializer.Meta):
        model = Section

class FullSimpleCodeSerializer(SimpleCodeSerializer):

 
    
    class Meta(SimpleCodeSerializer.Meta):
        model = SimpleCode

class FullAppliedChartSerializer(AppliedChartSerializer):

 
    
    class Meta(AppliedChartSerializer.Meta):
        model = AppliedChart

class FullChartSerializer(ChartSerializer):

 
    
    class Meta(ChartSerializer.Meta):
        model = Chart

class FullChartItemSerializer(ChartItemSerializer):

 
    
    class Meta(ChartItemSerializer.Meta):
        model = ChartItem

class FullChartProcedureSerializer(ChartProcedureSerializer):

 
    
    class Meta(ChartProcedureSerializer.Meta):
        model = ChartProcedure

class FullInvoiceSerializer(InvoiceSerializer):

 
    
    class Meta(InvoiceSerializer.Meta):
        model = Invoice

class FullServiceSerializer(ServiceSerializer):

 
    
    class Meta(ServiceSerializer.Meta):
        model = Service

class FullInvoiceItemSerializer(InvoiceItemSerializer):

 
    
    class Meta(InvoiceItemSerializer.Meta):
        model = InvoiceItem

class FullAppointmentSerializer(AppointmentSerializer):

 
    
    class Meta(AppointmentSerializer.Meta):
        model = Appointment

class FullAdmissionSerializer(AdmissionSerializer):

 
    encounter = EncounterSerializer(many=True, read_only=True)
 
    
    class Meta(AdmissionSerializer.Meta):
        model = Admission

class FullBedStaySerializer(BedStaySerializer):

 
    
    class Meta(BedStaySerializer.Meta):
        model = BedStay

class FullEmployeeSerializer(EmployeeSerializer):

 
    
    class Meta(EmployeeSerializer.Meta):
        model = Employee

class FullOrderTemplateSerializer(OrderTemplateSerializer):

 
    
    class Meta(OrderTemplateSerializer.Meta):
        model = OrderTemplate

class FullOrderSerializer(OrderSerializer):

 
    
    class Meta(OrderSerializer.Meta):
        model = Order

    
  