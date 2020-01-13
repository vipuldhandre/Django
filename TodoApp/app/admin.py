from django.contrib import admin
from app.models import Todoapp

class TodoappAdmin(admin.ModelAdmin):
    list_display=['content']

admin.site.register(Todoapp,TodoappAdmin)
# Register your models here.
