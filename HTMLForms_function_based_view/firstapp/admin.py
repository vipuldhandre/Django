from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','edes','esal']


admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
