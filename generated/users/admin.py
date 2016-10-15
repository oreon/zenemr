
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 



class AppUserAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class AppRoleAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class GroupAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(AppUser, AppUserAdmin)



admin.site.register(AppRole, AppRoleAdmin)



admin.site.register(Group, GroupAdmin)


 
