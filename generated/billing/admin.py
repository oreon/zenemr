
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem



class InvoiceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  InvoiceItemInline  ]
	
    

class ServiceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class InvoiceItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(Invoice, InvoiceAdmin)



admin.site.register(Service, ServiceAdmin)




 
