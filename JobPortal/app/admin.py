from django.contrib import admin
from app.models import Engineering,Management,Operations

class EngineeringAdmin(admin.ModelAdmin):
    list_display=['ejobs']

admin.site.register(Engineering,EngineeringAdmin)

class ManagementAdmin(admin.ModelAdmin):
    list_display=['mjobs']

admin.site.register(Management,ManagementAdmin)

class OperationsAdmin(admin.ModelAdmin):
    list_display=['ojobs']

admin.site.register(Operations,OperationsAdmin)

# Register your models here.
