from django.contrib import admin
from app.models import Company,Programmer,Languages

class CompanyAdmin(admin.ModelAdmin):
    list_display=['cname']

admin.site.register(Company,CompanyAdmin)

class ProgrammerAdmin(admin.ModelAdmin):
    list_display=['pname']

admin.site.register(Programmer,ProgrammerAdmin)

class LanguagesAdmin(admin.ModelAdmin):
    list_display=['lname']

admin.site.register(Languages,LanguagesAdmin)

# Register your models here.
