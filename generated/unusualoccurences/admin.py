
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 



class UnusualOccurenceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class OccurenceTypeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(UnusualOccurence, UnusualOccurenceAdmin)



admin.site.register(OccurenceType, OccurenceTypeAdmin)


 
