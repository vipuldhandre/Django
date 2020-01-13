from django.contrib import admin
from .models import Lecturer,Professor

class LecturerAdmin(admin.ModelAdmin):
    list_display=['lname','ledu','lfac','ldoj']

admin.site.register(Lecturer,LecturerAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display=['pname','pedu','pfac','pdoj']

admin.site.register(Professor,ProfessorAdmin)

# Register your models here.
