
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class ResultRowInline(admin.TabularInline):
    model = ResultRow

class RoomInline(admin.TabularInline):
    model = Room

class BedInline(admin.TabularInline):
    model = Bed

class WardInline(admin.TabularInline):
    model = Ward

class SettingNameInline(admin.TabularInline):
    model = SettingName

class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem

class PrescriptionItemTemplateInline(admin.TabularInline):
    model = PrescriptionItemTemplate

class AtcDrugInline(admin.TabularInline):
    model = AtcDrug

class DrugInteractionInline(admin.TabularInline):
    model = DrugInteraction

class DifferentialDxInline(admin.TabularInline):
    model = DifferentialDx

class PatientFindingInline(admin.TabularInline):
    model = PatientFinding

class CodeInline(admin.TabularInline):
    model = Code

class SectionInline(admin.TabularInline):
    model = Section

class ChartItemInline(admin.TabularInline):
    model = ChartItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem

class BedStayInline(admin.TabularInline):
    model = BedStay



class AppUserAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AppRoleAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class GroupAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class PatientAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class VaccinationAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class EncounterAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class VaccineAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class LabTestAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class TestResultsAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  ResultRowInline  ]
	
    

class ResultRowAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class FacilityAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  WardInline  ]
	
    

class RoomAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  BedInline  ]
	
    

class BedAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class WardAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  RoomInline  ]
	
    

class RoomTypeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class UnusualOccurenceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class OccurenceTypeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingsAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingNameAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingGroupAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  SettingNameInline  ]
	
    

class PrescriptionTemplateAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  PrescriptionItemTemplateInline  ]
	
    

class PrescriptionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  PrescriptionItemInline  ]
	
    

class PrescriptionItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class PrescriptionItemTemplateAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class FrequencyAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AtcDrugAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  AtcDrugInline  ]
	
    

class DrugAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  DrugInteractionInline  ]
	
    

class DrugInteractionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class DrugCategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class FindingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  DifferentialDxInline  ]
	
    

class PhysicalFindingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  DifferentialDxInline  ]
	
    

class LabFindingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  DifferentialDxInline  ]
	
    

class DiseaseAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ConditionFindingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ConditionCategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class DifferentialDxAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class DxCategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class PatientFindingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class PatientDiffDxAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  PatientFindingInline  ]
	
    

class DxTestAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChronicConditionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class CodeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChapterAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  SectionInline  ]
	
    

class SectionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  CodeInline  ]
	
    

class SimpleCodeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AppliedChartAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChartAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  ChartItemInline  ]
	
    

class ChartItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChartProcedureAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class InvoiceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  InvoiceItemInline  ]
	
    

class ServiceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class InvoiceItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AppointmentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AdmissionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  BedStayInline  ]
	
    

class BedStayAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class EmployeeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class OrderTemplateAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class OrderAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(AppUser, AppUserAdmin)



admin.site.register(AppRole, AppRoleAdmin)



admin.site.register(Group, GroupAdmin)



admin.site.register(Patient, PatientAdmin)



admin.site.register(Vaccination, VaccinationAdmin)



admin.site.register(Encounter, EncounterAdmin)



admin.site.register(Vaccine, VaccineAdmin)



admin.site.register(LabTest, LabTestAdmin)



admin.site.register(TestResults, TestResultsAdmin)





admin.site.register(Facility, FacilityAdmin)









admin.site.register(RoomType, RoomTypeAdmin)



admin.site.register(UnusualOccurence, UnusualOccurenceAdmin)



admin.site.register(OccurenceType, OccurenceTypeAdmin)



admin.site.register(Settings, SettingsAdmin)



admin.site.register(Setting, SettingAdmin)





admin.site.register(SettingGroup, SettingGroupAdmin)



admin.site.register(PrescriptionTemplate, PrescriptionTemplateAdmin)



admin.site.register(Prescription, PrescriptionAdmin)







admin.site.register(Frequency, FrequencyAdmin)





admin.site.register(Drug, DrugAdmin)





admin.site.register(DrugCategory, DrugCategoryAdmin)



admin.site.register(Finding, FindingAdmin)



admin.site.register(PhysicalFinding, PhysicalFindingAdmin)



admin.site.register(LabFinding, LabFindingAdmin)



admin.site.register(Disease, DiseaseAdmin)



admin.site.register(ConditionFinding, ConditionFindingAdmin)



admin.site.register(ConditionCategory, ConditionCategoryAdmin)





admin.site.register(DxCategory, DxCategoryAdmin)





admin.site.register(PatientDiffDx, PatientDiffDxAdmin)



admin.site.register(DxTest, DxTestAdmin)



admin.site.register(ChronicCondition, ChronicConditionAdmin)





admin.site.register(Chapter, ChapterAdmin)





admin.site.register(SimpleCode, SimpleCodeAdmin)



admin.site.register(AppliedChart, AppliedChartAdmin)



admin.site.register(Chart, ChartAdmin)





admin.site.register(ChartProcedure, ChartProcedureAdmin)



admin.site.register(Invoice, InvoiceAdmin)



admin.site.register(Service, ServiceAdmin)





admin.site.register(Appointment, AppointmentAdmin)



admin.site.register(Admission, AdmissionAdmin)





admin.site.register(Employee, EmployeeAdmin)



admin.site.register(OrderTemplate, OrderTemplateAdmin)



admin.site.register(Order, OrderAdmin)


 
