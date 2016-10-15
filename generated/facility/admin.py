
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class RoomInline(admin.TabularInline):
    model = Room

class BedInline(admin.TabularInline):
    model = Bed

class WardInline(admin.TabularInline):
    model = Ward



class FacilityAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  WardInline  ]
	
    

class RoomAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  BedInline  ]
	
    

class BedAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class WardAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  RoomInline  ]
	
    

class RoomTypeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    




admin.site.register(Facility, FacilityAdmin)









admin.site.register(RoomType, RoomTypeAdmin)


 
