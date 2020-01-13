from django.contrib import admin
from app.models import Tech,Sports,Politics

class TechAdmin(admin.ModelAdmin):
    list_display=['tnews']

admin.site.register(Tech,TechAdmin)

class SportsAdmin(admin.ModelAdmin):
    list_display=['snews']

admin.site.register(Sports,SportsAdmin)

class PoliticsAdmin(admin.ModelAdmin):
    list_display=['pnews']

admin.site.register(Politics,PoliticsAdmin)
# Register your models here.
