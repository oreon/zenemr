
 
from django.contrib import admin

from patients.models import *
from zenemr.commons import CustomModelAdminMixin

 
 
class DrugAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class CategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class PatientAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass



class PrescriptionItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem
    
class PrescriptionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    inlines = [ PrescriptionItemInline, ]
    
    
admin.site.register(Patient, PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Encounter)


    
    

class EmployeeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class VaccinationAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class EncounterAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class VaccineAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

 
 