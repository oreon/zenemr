
 
from django.contrib import admin

from .models import *
from commons.admin import CustomModelAdminMixin
 

class CodeInline(admin.TabularInline):
    model = Code

class SectionInline(admin.TabularInline):
    model = Section



class CodeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    

class ChapterAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  SectionInline  ]
	
    

class SectionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	inlines = [  CodeInline  ]
	
    

class SimpleCodeAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	
	pass
	
    






admin.site.register(Chapter, ChapterAdmin)





admin.site.register(SimpleCode, SimpleCodeAdmin)


 
