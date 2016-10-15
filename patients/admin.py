
 
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, \
    NestedTabularInline

from commons.admin import CustomModelAdminMixin
from patients.models import *


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
    
    

    
    

class EmployeeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class VaccinationAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class VaccineAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

class VaccinationInline(admin.StackedInline):
    model = Vaccination
    

class PrescriptionItemInlineNested(NestedTabularInline):
    model = PrescriptionItem

class PrescriptionInline(NestedStackedInline):
    model = Prescription
    inlines = [PrescriptionItemInlineNested ]


class EncounterAdmin(CustomModelAdminMixin, NestedModelAdmin):
    model = Encounter
    inlines = [PrescriptionInline ]
    
 
admin.site.register(Patient, PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(Vaccine, VaccineAdmin)
