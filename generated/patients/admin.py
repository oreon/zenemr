
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class ResultRowInline(admin.TabularInline):
    model = ResultRow



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
	
    




admin.site.register(Patient, PatientAdmin)



admin.site.register(Vaccination, VaccinationAdmin)



admin.site.register(Encounter, EncounterAdmin)



admin.site.register(Vaccine, VaccineAdmin)



admin.site.register(LabTest, LabTestAdmin)



admin.site.register(TestResults, TestResultsAdmin)




 
