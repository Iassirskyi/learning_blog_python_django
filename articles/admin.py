from django.contrib import admin
from .models import Article, Entry

admin.site.register(Article)
#admin.site.register(Entry)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title']
