from django.contrib import admin

from .models import Publish


# Register your models here.
@admin.register(Publish)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'user')
    list_filter = ('published', 'user')
    search_fields = ('title', 'content')
    raw_id_fields = ('user',)
    readonly_fields = ['published_date']
    list_editable = ['published']
