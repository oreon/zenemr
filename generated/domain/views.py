
from rest_framework import viewsets
from .serializers import *
    
class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    
class AppUserLookupViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserLookupSerializer
    
class AppUserCompleteViewSet(AppUserViewSet):
    serializer_class = FullAppUserSerializer
    
class AppUserWritableViewSet(AppUserViewSet):
    serializer_class = AppUserWritableSerializer    

class AppRoleViewSet(viewsets.ModelViewSet):
    queryset = AppRole.objects.all()
    serializer_class = AppRoleSerializer
    
class AppRoleLookupViewSet(viewsets.ModelViewSet):
    queryset = AppRole.objects.all()
    serializer_class = AppRoleLookupSerializer
    
class AppRoleCompleteViewSet(AppRoleViewSet):
    serializer_class = FullAppRoleSerializer
    
class AppRoleWritableViewSet(AppRoleViewSet):
    serializer_class = AppRoleWritableSerializer    

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class GroupLookupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupLookupSerializer
    
class GroupCompleteViewSet(GroupViewSet):
    serializer_class = FullGroupSerializer
    
class GroupWritableViewSet(GroupViewSet):
    serializer_class = GroupWritableSerializer    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class PatientLookupViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientLookupSerializer
    
class PatientCompleteViewSet(PatientViewSet):
    serializer_class = FullPatientSerializer
    
class PatientWritableViewSet(PatientViewSet):
    serializer_class = PatientWritableSerializer    

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    
class VaccinationLookupViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationLookupSerializer
    
class VaccinationCompleteViewSet(VaccinationViewSet):
    serializer_class = FullVaccinationSerializer
    
class VaccinationWritableViewSet(VaccinationViewSet):
    serializer_class = VaccinationWritableSerializer    

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    
class EncounterLookupViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterLookupSerializer
    
class EncounterCompleteViewSet(EncounterViewSet):
    serializer_class = FullEncounterSerializer
    
class EncounterWritableViewSet(EncounterViewSet):
    serializer_class = EncounterWritableSerializer    

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    
class VaccineLookupViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineLookupSerializer
    
class VaccineCompleteViewSet(VaccineViewSet):
    serializer_class = FullVaccineSerializer
    
class VaccineWritableViewSet(VaccineViewSet):
    serializer_class = VaccineWritableSerializer    

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer
    
class LabTestLookupViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestLookupSerializer
    
class LabTestCompleteViewSet(LabTestViewSet):
    serializer_class = FullLabTestSerializer
    
class LabTestWritableViewSet(LabTestViewSet):
    serializer_class = LabTestWritableSerializer    

class TestResultsViewSet(viewsets.ModelViewSet):
    queryset = TestResults.objects.all()
    serializer_class = TestResultsSerializer
    
class TestResultsLookupViewSet(viewsets.ModelViewSet):
    queryset = TestResults.objects.all()
    serializer_class = TestResultsLookupSerializer
    
class TestResultsCompleteViewSet(TestResultsViewSet):
    serializer_class = FullTestResultsSerializer
    
class TestResultsWritableViewSet(TestResultsViewSet):
    serializer_class = TestResultsWritableSerializer    

class ResultRowViewSet(viewsets.ModelViewSet):
    queryset = ResultRow.objects.all()
    serializer_class = ResultRowSerializer
    
class ResultRowLookupViewSet(viewsets.ModelViewSet):
    queryset = ResultRow.objects.all()
    serializer_class = ResultRowLookupSerializer
    
class ResultRowCompleteViewSet(ResultRowViewSet):
    serializer_class = FullResultRowSerializer
    
class ResultRowWritableViewSet(ResultRowViewSet):
    serializer_class = ResultRowWritableSerializer    

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    
class FacilityLookupViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilityLookupSerializer
    
class FacilityCompleteViewSet(FacilityViewSet):
    serializer_class = FullFacilitySerializer
    
class FacilityWritableViewSet(FacilityViewSet):
    serializer_class = FacilityWritableSerializer    

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class RoomLookupViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomLookupSerializer
    
class RoomCompleteViewSet(RoomViewSet):
    serializer_class = FullRoomSerializer
    
class RoomWritableViewSet(RoomViewSet):
    serializer_class = RoomWritableSerializer    

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    
class BedLookupViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedLookupSerializer
    
class BedCompleteViewSet(BedViewSet):
    serializer_class = FullBedSerializer
    
class BedWritableViewSet(BedViewSet):
    serializer_class = BedWritableSerializer    

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    
class WardLookupViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardLookupSerializer
    
class WardCompleteViewSet(WardViewSet):
    serializer_class = FullWardSerializer
    
class WardWritableViewSet(WardViewSet):
    serializer_class = WardWritableSerializer    

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    
class RoomTypeLookupViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeLookupSerializer
    
class RoomTypeCompleteViewSet(RoomTypeViewSet):
    serializer_class = FullRoomTypeSerializer
    
class RoomTypeWritableViewSet(RoomTypeViewSet):
    serializer_class = RoomTypeWritableSerializer    

class UnusualOccurenceViewSet(viewsets.ModelViewSet):
    queryset = UnusualOccurence.objects.all()
    serializer_class = UnusualOccurenceSerializer
    
class UnusualOccurenceLookupViewSet(viewsets.ModelViewSet):
    queryset = UnusualOccurence.objects.all()
    serializer_class = UnusualOccurenceLookupSerializer
    
class UnusualOccurenceCompleteViewSet(UnusualOccurenceViewSet):
    serializer_class = FullUnusualOccurenceSerializer
    
class UnusualOccurenceWritableViewSet(UnusualOccurenceViewSet):
    serializer_class = UnusualOccurenceWritableSerializer    

class OccurenceTypeViewSet(viewsets.ModelViewSet):
    queryset = OccurenceType.objects.all()
    serializer_class = OccurenceTypeSerializer
    
class OccurenceTypeLookupViewSet(viewsets.ModelViewSet):
    queryset = OccurenceType.objects.all()
    serializer_class = OccurenceTypeLookupSerializer
    
class OccurenceTypeCompleteViewSet(OccurenceTypeViewSet):
    serializer_class = FullOccurenceTypeSerializer
    
class OccurenceTypeWritableViewSet(OccurenceTypeViewSet):
    serializer_class = OccurenceTypeWritableSerializer    

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    
class SettingsLookupViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsLookupSerializer
    
class SettingsCompleteViewSet(SettingsViewSet):
    serializer_class = FullSettingsSerializer
    
class SettingsWritableViewSet(SettingsViewSet):
    serializer_class = SettingsWritableSerializer    

class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    
class SettingLookupViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingLookupSerializer
    
class SettingCompleteViewSet(SettingViewSet):
    serializer_class = FullSettingSerializer
    
class SettingWritableViewSet(SettingViewSet):
    serializer_class = SettingWritableSerializer    

class SettingNameViewSet(viewsets.ModelViewSet):
    queryset = SettingName.objects.all()
    serializer_class = SettingNameSerializer
    
class SettingNameLookupViewSet(viewsets.ModelViewSet):
    queryset = SettingName.objects.all()
    serializer_class = SettingNameLookupSerializer
    
class SettingNameCompleteViewSet(SettingNameViewSet):
    serializer_class = FullSettingNameSerializer
    
class SettingNameWritableViewSet(SettingNameViewSet):
    serializer_class = SettingNameWritableSerializer    

class SettingGroupViewSet(viewsets.ModelViewSet):
    queryset = SettingGroup.objects.all()
    serializer_class = SettingGroupSerializer
    
class SettingGroupLookupViewSet(viewsets.ModelViewSet):
    queryset = SettingGroup.objects.all()
    serializer_class = SettingGroupLookupSerializer
    
class SettingGroupCompleteViewSet(SettingGroupViewSet):
    serializer_class = FullSettingGroupSerializer
    
class SettingGroupWritableViewSet(SettingGroupViewSet):
    serializer_class = SettingGroupWritableSerializer    

class PrescriptionTemplateViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionTemplate.objects.all()
    serializer_class = PrescriptionTemplateSerializer
    
class PrescriptionTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionTemplate.objects.all()
    serializer_class = PrescriptionTemplateLookupSerializer
    
class PrescriptionTemplateCompleteViewSet(PrescriptionTemplateViewSet):
    serializer_class = FullPrescriptionTemplateSerializer
    
class PrescriptionTemplateWritableViewSet(PrescriptionTemplateViewSet):
    serializer_class = PrescriptionTemplateWritableSerializer    

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class PrescriptionLookupViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionLookupSerializer
    
class PrescriptionCompleteViewSet(PrescriptionViewSet):
    serializer_class = FullPrescriptionSerializer
    
class PrescriptionWritableViewSet(PrescriptionViewSet):
    serializer_class = PrescriptionWritableSerializer    

class PrescriptionItemViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemSerializer
    
class PrescriptionItemLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemLookupSerializer
    
class PrescriptionItemCompleteViewSet(PrescriptionItemViewSet):
    serializer_class = FullPrescriptionItemSerializer
    
class PrescriptionItemWritableViewSet(PrescriptionItemViewSet):
    serializer_class = PrescriptionItemWritableSerializer    

class PrescriptionItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItemTemplate.objects.all()
    serializer_class = PrescriptionItemTemplateSerializer
    
class PrescriptionItemTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItemTemplate.objects.all()
    serializer_class = PrescriptionItemTemplateLookupSerializer
    
class PrescriptionItemTemplateCompleteViewSet(PrescriptionItemTemplateViewSet):
    serializer_class = FullPrescriptionItemTemplateSerializer
    
class PrescriptionItemTemplateWritableViewSet(PrescriptionItemTemplateViewSet):
    serializer_class = PrescriptionItemTemplateWritableSerializer    

class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
    
class FrequencyLookupViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencyLookupSerializer
    
class FrequencyCompleteViewSet(FrequencyViewSet):
    serializer_class = FullFrequencySerializer
    
class FrequencyWritableViewSet(FrequencyViewSet):
    serializer_class = FrequencyWritableSerializer    

class AtcDrugViewSet(viewsets.ModelViewSet):
    queryset = AtcDrug.objects.all()
    serializer_class = AtcDrugSerializer
    
class AtcDrugLookupViewSet(viewsets.ModelViewSet):
    queryset = AtcDrug.objects.all()
    serializer_class = AtcDrugLookupSerializer
    
class AtcDrugCompleteViewSet(AtcDrugViewSet):
    serializer_class = FullAtcDrugSerializer
    
class AtcDrugWritableViewSet(AtcDrugViewSet):
    serializer_class = AtcDrugWritableSerializer    

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    
class DrugLookupViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugLookupSerializer
    
class DrugCompleteViewSet(DrugViewSet):
    serializer_class = FullDrugSerializer
    
class DrugWritableViewSet(DrugViewSet):
    serializer_class = DrugWritableSerializer    

class DrugInteractionViewSet(viewsets.ModelViewSet):
    queryset = DrugInteraction.objects.all()
    serializer_class = DrugInteractionSerializer
    
class DrugInteractionLookupViewSet(viewsets.ModelViewSet):
    queryset = DrugInteraction.objects.all()
    serializer_class = DrugInteractionLookupSerializer
    
class DrugInteractionCompleteViewSet(DrugInteractionViewSet):
    serializer_class = FullDrugInteractionSerializer
    
class DrugInteractionWritableViewSet(DrugInteractionViewSet):
    serializer_class = DrugInteractionWritableSerializer    

class DrugCategoryViewSet(viewsets.ModelViewSet):
    queryset = DrugCategory.objects.all()
    serializer_class = DrugCategorySerializer
    
class DrugCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = DrugCategory.objects.all()
    serializer_class = DrugCategoryLookupSerializer
    
class DrugCategoryCompleteViewSet(DrugCategoryViewSet):
    serializer_class = FullDrugCategorySerializer
    
class DrugCategoryWritableViewSet(DrugCategoryViewSet):
    serializer_class = DrugCategoryWritableSerializer    

class FindingViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class FindingLookupViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingLookupSerializer
    
class FindingCompleteViewSet(FindingViewSet):
    serializer_class = FullFindingSerializer
    
class FindingWritableViewSet(FindingViewSet):
    serializer_class = FindingWritableSerializer    

class PhysicalFindingViewSet(viewsets.ModelViewSet):
    queryset = PhysicalFinding.objects.all()
    serializer_class = PhysicalFindingSerializer
    
class PhysicalFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = PhysicalFinding.objects.all()
    serializer_class = PhysicalFindingLookupSerializer
    
class PhysicalFindingCompleteViewSet(PhysicalFindingViewSet):
    serializer_class = FullPhysicalFindingSerializer
    
class PhysicalFindingWritableViewSet(PhysicalFindingViewSet):
    serializer_class = PhysicalFindingWritableSerializer    

class LabFindingViewSet(viewsets.ModelViewSet):
    queryset = LabFinding.objects.all()
    serializer_class = LabFindingSerializer
    
class LabFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = LabFinding.objects.all()
    serializer_class = LabFindingLookupSerializer
    
class LabFindingCompleteViewSet(LabFindingViewSet):
    serializer_class = FullLabFindingSerializer
    
class LabFindingWritableViewSet(LabFindingViewSet):
    serializer_class = LabFindingWritableSerializer    

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    
class DiseaseLookupViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseLookupSerializer
    
class DiseaseCompleteViewSet(DiseaseViewSet):
    serializer_class = FullDiseaseSerializer
    
class DiseaseWritableViewSet(DiseaseViewSet):
    serializer_class = DiseaseWritableSerializer    

class ConditionFindingViewSet(viewsets.ModelViewSet):
    queryset = ConditionFinding.objects.all()
    serializer_class = ConditionFindingSerializer
    
class ConditionFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = ConditionFinding.objects.all()
    serializer_class = ConditionFindingLookupSerializer
    
class ConditionFindingCompleteViewSet(ConditionFindingViewSet):
    serializer_class = FullConditionFindingSerializer
    
class ConditionFindingWritableViewSet(ConditionFindingViewSet):
    serializer_class = ConditionFindingWritableSerializer    

class ConditionCategoryViewSet(viewsets.ModelViewSet):
    queryset = ConditionCategory.objects.all()
    serializer_class = ConditionCategorySerializer
    
class ConditionCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = ConditionCategory.objects.all()
    serializer_class = ConditionCategoryLookupSerializer
    
class ConditionCategoryCompleteViewSet(ConditionCategoryViewSet):
    serializer_class = FullConditionCategorySerializer
    
class ConditionCategoryWritableViewSet(ConditionCategoryViewSet):
    serializer_class = ConditionCategoryWritableSerializer    

class DifferentialDxViewSet(viewsets.ModelViewSet):
    queryset = DifferentialDx.objects.all()
    serializer_class = DifferentialDxSerializer
    
class DifferentialDxLookupViewSet(viewsets.ModelViewSet):
    queryset = DifferentialDx.objects.all()
    serializer_class = DifferentialDxLookupSerializer
    
class DifferentialDxCompleteViewSet(DifferentialDxViewSet):
    serializer_class = FullDifferentialDxSerializer
    
class DifferentialDxWritableViewSet(DifferentialDxViewSet):
    serializer_class = DifferentialDxWritableSerializer    

class DxCategoryViewSet(viewsets.ModelViewSet):
    queryset = DxCategory.objects.all()
    serializer_class = DxCategorySerializer
    
class DxCategoryLookupViewSet(viewsets.ModelViewSet):
    queryset = DxCategory.objects.all()
    serializer_class = DxCategoryLookupSerializer
    
class DxCategoryCompleteViewSet(DxCategoryViewSet):
    serializer_class = FullDxCategorySerializer
    
class DxCategoryWritableViewSet(DxCategoryViewSet):
    serializer_class = DxCategoryWritableSerializer    

class PatientFindingViewSet(viewsets.ModelViewSet):
    queryset = PatientFinding.objects.all()
    serializer_class = PatientFindingSerializer
    
class PatientFindingLookupViewSet(viewsets.ModelViewSet):
    queryset = PatientFinding.objects.all()
    serializer_class = PatientFindingLookupSerializer
    
class PatientFindingCompleteViewSet(PatientFindingViewSet):
    serializer_class = FullPatientFindingSerializer
    
class PatientFindingWritableViewSet(PatientFindingViewSet):
    serializer_class = PatientFindingWritableSerializer    

class PatientDiffDxViewSet(viewsets.ModelViewSet):
    queryset = PatientDiffDx.objects.all()
    serializer_class = PatientDiffDxSerializer
    
class PatientDiffDxLookupViewSet(viewsets.ModelViewSet):
    queryset = PatientDiffDx.objects.all()
    serializer_class = PatientDiffDxLookupSerializer
    
class PatientDiffDxCompleteViewSet(PatientDiffDxViewSet):
    serializer_class = FullPatientDiffDxSerializer
    
class PatientDiffDxWritableViewSet(PatientDiffDxViewSet):
    serializer_class = PatientDiffDxWritableSerializer    

class DxTestViewSet(viewsets.ModelViewSet):
    queryset = DxTest.objects.all()
    serializer_class = DxTestSerializer
    
class DxTestLookupViewSet(viewsets.ModelViewSet):
    queryset = DxTest.objects.all()
    serializer_class = DxTestLookupSerializer
    
class DxTestCompleteViewSet(DxTestViewSet):
    serializer_class = FullDxTestSerializer
    
class DxTestWritableViewSet(DxTestViewSet):
    serializer_class = DxTestWritableSerializer    

class ChronicConditionViewSet(viewsets.ModelViewSet):
    queryset = ChronicCondition.objects.all()
    serializer_class = ChronicConditionSerializer
    
class ChronicConditionLookupViewSet(viewsets.ModelViewSet):
    queryset = ChronicCondition.objects.all()
    serializer_class = ChronicConditionLookupSerializer
    
class ChronicConditionCompleteViewSet(ChronicConditionViewSet):
    serializer_class = FullChronicConditionSerializer
    
class ChronicConditionWritableViewSet(ChronicConditionViewSet):
    serializer_class = ChronicConditionWritableSerializer    

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    
class CodeLookupViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeLookupSerializer
    
class CodeCompleteViewSet(CodeViewSet):
    serializer_class = FullCodeSerializer
    
class CodeWritableViewSet(CodeViewSet):
    serializer_class = CodeWritableSerializer    

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    
class ChapterLookupViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterLookupSerializer
    
class ChapterCompleteViewSet(ChapterViewSet):
    serializer_class = FullChapterSerializer
    
class ChapterWritableViewSet(ChapterViewSet):
    serializer_class = ChapterWritableSerializer    

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    
class SectionLookupViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionLookupSerializer
    
class SectionCompleteViewSet(SectionViewSet):
    serializer_class = FullSectionSerializer
    
class SectionWritableViewSet(SectionViewSet):
    serializer_class = SectionWritableSerializer    

class SimpleCodeViewSet(viewsets.ModelViewSet):
    queryset = SimpleCode.objects.all()
    serializer_class = SimpleCodeSerializer
    
class SimpleCodeLookupViewSet(viewsets.ModelViewSet):
    queryset = SimpleCode.objects.all()
    serializer_class = SimpleCodeLookupSerializer
    
class SimpleCodeCompleteViewSet(SimpleCodeViewSet):
    serializer_class = FullSimpleCodeSerializer
    
class SimpleCodeWritableViewSet(SimpleCodeViewSet):
    serializer_class = SimpleCodeWritableSerializer    

class AppliedChartViewSet(viewsets.ModelViewSet):
    queryset = AppliedChart.objects.all()
    serializer_class = AppliedChartSerializer
    
class AppliedChartLookupViewSet(viewsets.ModelViewSet):
    queryset = AppliedChart.objects.all()
    serializer_class = AppliedChartLookupSerializer
    
class AppliedChartCompleteViewSet(AppliedChartViewSet):
    serializer_class = FullAppliedChartSerializer
    
class AppliedChartWritableViewSet(AppliedChartViewSet):
    serializer_class = AppliedChartWritableSerializer    

class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    
class ChartLookupViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartLookupSerializer
    
class ChartCompleteViewSet(ChartViewSet):
    serializer_class = FullChartSerializer
    
class ChartWritableViewSet(ChartViewSet):
    serializer_class = ChartWritableSerializer    

class ChartItemViewSet(viewsets.ModelViewSet):
    queryset = ChartItem.objects.all()
    serializer_class = ChartItemSerializer
    
class ChartItemLookupViewSet(viewsets.ModelViewSet):
    queryset = ChartItem.objects.all()
    serializer_class = ChartItemLookupSerializer
    
class ChartItemCompleteViewSet(ChartItemViewSet):
    serializer_class = FullChartItemSerializer
    
class ChartItemWritableViewSet(ChartItemViewSet):
    serializer_class = ChartItemWritableSerializer    

class ChartProcedureViewSet(viewsets.ModelViewSet):
    queryset = ChartProcedure.objects.all()
    serializer_class = ChartProcedureSerializer
    
class ChartProcedureLookupViewSet(viewsets.ModelViewSet):
    queryset = ChartProcedure.objects.all()
    serializer_class = ChartProcedureLookupSerializer
    
class ChartProcedureCompleteViewSet(ChartProcedureViewSet):
    serializer_class = FullChartProcedureSerializer
    
class ChartProcedureWritableViewSet(ChartProcedureViewSet):
    serializer_class = ChartProcedureWritableSerializer    

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class InvoiceLookupViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceLookupSerializer
    
class InvoiceCompleteViewSet(InvoiceViewSet):
    serializer_class = FullInvoiceSerializer
    
class InvoiceWritableViewSet(InvoiceViewSet):
    serializer_class = InvoiceWritableSerializer    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceLookupViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceLookupSerializer
    
class ServiceCompleteViewSet(ServiceViewSet):
    serializer_class = FullServiceSerializer
    
class ServiceWritableViewSet(ServiceViewSet):
    serializer_class = ServiceWritableSerializer    

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    
class InvoiceItemLookupViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemLookupSerializer
    
class InvoiceItemCompleteViewSet(InvoiceItemViewSet):
    serializer_class = FullInvoiceItemSerializer
    
class InvoiceItemWritableViewSet(InvoiceItemViewSet):
    serializer_class = InvoiceItemWritableSerializer    

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class AppointmentLookupViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentLookupSerializer
    
class AppointmentCompleteViewSet(AppointmentViewSet):
    serializer_class = FullAppointmentSerializer
    
class AppointmentWritableViewSet(AppointmentViewSet):
    serializer_class = AppointmentWritableSerializer    

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    
class AdmissionLookupViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionLookupSerializer
    
class AdmissionCompleteViewSet(AdmissionViewSet):
    serializer_class = FullAdmissionSerializer
    
class AdmissionWritableViewSet(AdmissionViewSet):
    serializer_class = AdmissionWritableSerializer    

class BedStayViewSet(viewsets.ModelViewSet):
    queryset = BedStay.objects.all()
    serializer_class = BedStaySerializer
    
class BedStayLookupViewSet(viewsets.ModelViewSet):
    queryset = BedStay.objects.all()
    serializer_class = BedStayLookupSerializer
    
class BedStayCompleteViewSet(BedStayViewSet):
    serializer_class = FullBedStaySerializer
    
class BedStayWritableViewSet(BedStayViewSet):
    serializer_class = BedStayWritableSerializer    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeLookupViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeLookupSerializer
    
class EmployeeCompleteViewSet(EmployeeViewSet):
    serializer_class = FullEmployeeSerializer
    
class EmployeeWritableViewSet(EmployeeViewSet):
    serializer_class = EmployeeWritableSerializer    

class OrderTemplateViewSet(viewsets.ModelViewSet):
    queryset = OrderTemplate.objects.all()
    serializer_class = OrderTemplateSerializer
    
class OrderTemplateLookupViewSet(viewsets.ModelViewSet):
    queryset = OrderTemplate.objects.all()
    serializer_class = OrderTemplateLookupSerializer
    
class OrderTemplateCompleteViewSet(OrderTemplateViewSet):
    serializer_class = FullOrderTemplateSerializer
    
class OrderTemplateWritableViewSet(OrderTemplateViewSet):
    serializer_class = OrderTemplateWritableSerializer    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderLookupViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderLookupSerializer
    
class OrderCompleteViewSet(OrderViewSet):
    serializer_class = FullOrderSerializer
    
class OrderWritableViewSet(OrderViewSet):
    serializer_class = OrderWritableSerializer    

  