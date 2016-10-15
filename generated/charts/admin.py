
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class ChartItemInline(admin.TabularInline):
    model = ChartItem



class AppliedChartAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChartAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  ChartItemInline  ]
	
    

class ChartItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChartProcedureAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(AppliedChart, AppliedChartAdmin)



admin.site.register(Chart, ChartAdmin)





admin.site.register(ChartProcedure, ChartProcedureAdmin)


 
