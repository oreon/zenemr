
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 



class OrderTemplateAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class OrderAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(OrderTemplate, OrderTemplateAdmin)



admin.site.register(Order, OrderAdmin)


 
