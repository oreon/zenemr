
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem

class PrescriptionItemTemplateInline(admin.TabularInline):
    model = PrescriptionItemTemplate



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
	
    




admin.site.register(PrescriptionTemplate, PrescriptionTemplateAdmin)



admin.site.register(Prescription, PrescriptionAdmin)







admin.site.register(Frequency, FrequencyAdmin)


 
