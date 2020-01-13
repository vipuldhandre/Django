from django.contrib import admin
from .models import Student,Employee


class StudentAdmin(admin.ModelAdmin):
    list_display=['name','address','rollno','school']

admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','eaddr','emobno']

admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
