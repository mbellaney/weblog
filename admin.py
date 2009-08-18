from django.contrib import admin
from weblog.models import Category, Entry, Link

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Entry, EntryAdmin)

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)



