from django.contrib import admin
from app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sname','srn','sclass','smarks']

admin.site.register(Student,StudentAdmin)

# Register your models here.
