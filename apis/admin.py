from django.contrib import admin

from apis.models import studentModel 

# Register your models here.
class appAdmin(admin.ModelAdmin):
        
    list_display=['name','gender','classes','father_information']

admin.site.register(studentModel,appAdmin)


