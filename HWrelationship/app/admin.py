from django.contrib import admin
from app.models import University,College,Department

class UniversityAdmin(admin.ModelAdmin):
    list_display=['uname']

admin.site.register(University,UniversityAdmin)


class CollegeAdmin(admin.ModelAdmin):
    list_display=['cname']

admin.site.register(College,CollegeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display=['dname']

admin.site.register(Department,DepartmentAdmin)

# Register your models here.
