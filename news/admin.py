from django.contrib import admin
from .models import NewsDetail
# Register your models here.
class NewsDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'publisher', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('publisher', 'title',)
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(NewsDetail, NewsDetailAdmin)
