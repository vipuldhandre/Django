from django.contrib import admin
from app.models import *

class CourseAdmin(admin.ModelAdmin):
    list_display=['cname']

admin.site.register(Course,CourseAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display=['fname']

admin.site.register(Faculty,FacultyAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_display=['bname']

admin.site.register(Batch,BatchAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['sname']

admin.site.register(Student,StudentAdmin)

# Register your models here.
