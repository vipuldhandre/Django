from django.contrib import admin
from app.models import Stusearch

class StusearchAdmin(admin.ModelAdmin):
    list_display=['stuname']

admin.site.register(Stusearch,StusearchAdmin)

# Register your models here.
