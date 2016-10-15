
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class AtcDrugInline(admin.TabularInline):
    model = AtcDrug

class DrugInteractionInline(admin.TabularInline):
    model = DrugInteraction



class AtcDrugAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  AtcDrugInline  ]
	
    

class DrugAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  DrugInteractionInline  ]
	
    

class DrugInteractionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class DrugCategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    






admin.site.register(Drug, DrugAdmin)





admin.site.register(DrugCategory, DrugCategoryAdmin)


 
