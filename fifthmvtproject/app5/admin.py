from django.contrib import admin
from .models import Tester,Developer

class TesterAdmin(admin.ModelAdmin):
    list_display=['tname','tdes','tproject','tdoj']

admin.site.register(Tester,TesterAdmin)

class DeveloperAdmin(admin.ModelAdmin):
    list_display=['dname','ddes','dproject','ddoj']

admin.site.register(Developer,DeveloperAdmin)

# Register your models here.
