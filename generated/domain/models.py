
from django.db import models
from .modelsBase import *
    
class AppUser(AppUserBase): 
        pass
    

class AppRole(AppRoleBase): 
        pass
    

class Group(GroupBase): 
        pass
    

class Patient(PatientBase): 
        pass
    

class Person(PersonBase): 
    class Meta:
        abstract = True
    

class Vaccination(VaccinationBase): 
        pass
    

class Encounter(EncounterBase): 
        pass
    

class Vaccine(VaccineBase): 
        pass
    

class LabTest(LabTestBase): 
        pass
    

class TestResults(TestResultsBase): 
        pass
    

class ResultRow(ResultRowBase): 
        pass
    

class Facility(FacilityBase): 
        pass
    

class Room(RoomBase): 
        pass
    

class Bed(BedBase): 
        pass
    

class Ward(WardBase): 
        pass
    

class RoomType(RoomTypeBase): 
        pass
    

class UnusualOccurence(UnusualOccurenceBase): 
        pass
    

class OccurenceType(OccurenceTypeBase): 
        pass
    

class Settings(SettingsBase): 
        pass
    

class Setting(SettingBase): 
        pass
    

class SettingName(SettingNameBase): 
        pass
    

class SettingGroup(SettingGroupBase): 
        pass
    

class PrescriptionTemplate(PrescriptionTemplateBase): 
        pass
    

class Prescription(PrescriptionBase): 
        pass
    

class PrescriptionItem(PrescriptionItemBase): 
        pass
    

class PrescriptionItemTemplate(PrescriptionItemTemplateBase): 
        pass
    

class Frequency(FrequencyBase): 
        pass
    

class AtcDrug(AtcDrugBase): 
        pass
    

class Drug(DrugBase): 
        pass
    

class DrugInteraction(DrugInteractionBase): 
        pass
    

class DrugCategory(DrugCategoryBase): 
        pass
    

class Finding(FindingBase): 
        pass
    

class PhysicalFinding(PhysicalFindingBase): 
        pass
    

class LabFinding(LabFindingBase): 
        pass
    

class Disease(DiseaseBase): 
        pass
    

class ConditionFinding(ConditionFindingBase): 
        pass
    

class ConditionCategory(ConditionCategoryBase): 
        pass
    

class DifferentialDx(DifferentialDxBase): 
        pass
    

class DxCategory(DxCategoryBase): 
        pass
    

class PatientFinding(PatientFindingBase): 
        pass
    

class PatientDiffDx(PatientDiffDxBase): 
        pass
    

class DxTest(DxTestBase): 
        pass
    

class ChronicCondition(ChronicConditionBase): 
        pass
    

class Code(CodeBase): 
        pass
    

class Chapter(ChapterBase): 
        pass
    

class Section(SectionBase): 
        pass
    

class AbstractCode(AbstractCodeBase): 
        pass
    

class SimpleCode(SimpleCodeBase): 
        pass
    

class AppliedChart(AppliedChartBase): 
        pass
    

class Chart(ChartBase): 
        pass
    

class ChartItem(ChartItemBase): 
        pass
    

class ChartProcedure(ChartProcedureBase): 
        pass
    

class Invoice(InvoiceBase): 
        pass
    

class Service(ServiceBase): 
        pass
    

class InvoiceItem(InvoiceItemBase): 
        pass
    

class Appointment(AppointmentBase): 
        pass
    

class Admission(AdmissionBase): 
        pass
    

class BedStay(BedStayBase): 
        pass
    

class Employee(EmployeeBase): 
        pass
    

class OrderTemplate(OrderTemplateBase): 
        pass
    

class Order(OrderBase): 
        pass
    

  