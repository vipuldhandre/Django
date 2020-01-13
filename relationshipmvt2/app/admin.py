from django.contrib import admin
from app.models import Language,Framework,Actor,Movie

class LanguageAdmin(admin.ModelAdmin):
    list_display=['lname']

admin.site.register(Language,LanguageAdmin)

class FrameworkAdmin(admin.ModelAdmin):
    list_display=['fname']

admin.site.register(Framework,FrameworkAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display=['mname']

admin.site.register(Movie,MovieAdmin)


class ActorAdmin(admin.ModelAdmin):
    list_display=['aname']

admin.site.register(Actor,ActorAdmin)
# Register your models here.
