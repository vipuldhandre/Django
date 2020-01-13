from django.contrib import admin
from app.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display=['bname','bauthor','bprice']

admin.site.register(Book,BookAdmin)

# Register your models here.
