from django.contrib import admin
from app import models

class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'classroom_id', 'parent_id')
    
# Register your models here.
admin.site.register(models.Parent, ParentAdmin)
admin.site.register(models.Student, StudentAdmin)