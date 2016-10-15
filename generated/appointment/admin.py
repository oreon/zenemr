
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 



class AppointmentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(Appointment, AppointmentAdmin)


 
