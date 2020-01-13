from django.contrib import admin
from .models import Student,Employee


class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','srn','sclass','sschool']

admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','eeid','eaddr']

admin.site.register(Employee,EmployeeAdmin)

# Register your models here.
