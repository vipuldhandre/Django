from django.contrib import admin
from .models import Book,Mobile

class BookAdmin(admin.ModelAdmin):
    list_display=['bname','bprice','bauthor']

admin.site.register(Book,BookAdmin)

class MobileAdmin(admin.ModelAdmin):
    list_display=['mname','mmodel','mprice']

admin.site.register(Mobile,MobileAdmin)

# Register your models here.
