
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class SettingNameInline(admin.TabularInline):
    model = SettingName



class SettingsAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingNameAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class SettingGroupAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  SettingNameInline  ]
	
    




admin.site.register(Settings, SettingsAdmin)



admin.site.register(Setting, SettingAdmin)





admin.site.register(SettingGroup, SettingGroupAdmin)


 
