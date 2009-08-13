from django.contrib import admin
from weblog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Entry, EntryAdmin)


