
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 



class EmployeeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(Employee, EmployeeAdmin)


 
