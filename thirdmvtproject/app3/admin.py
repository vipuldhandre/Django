from django.contrib import admin
from .models import Born,Human

class BornAdmin(admin.ModelAdmin):
    list_display=['bname','bdate','bcity']

admin.site.register(Born,BornAdmin)

class HumanAdmin(admin.ModelAdmin):
    list_display=['hname','htype','hcity','haddr']

admin.site.register(Human,HumanAdmin)
# Register your models here.
