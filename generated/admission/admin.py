
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class BedStayInline(admin.TabularInline):
    model = BedStay



class AdmissionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  BedStayInline  ]
	
    

class BedStayAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(Admission, AdmissionAdmin)




 
