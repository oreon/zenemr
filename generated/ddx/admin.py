
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class DifferentialDxInline(admin.TabularInline):
    model = DifferentialDx

class PatientFindingInline(admin.TabularInline):
    model = PatientFinding



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


 
