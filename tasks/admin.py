from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description_short', 'status', 'created_at')
    list_display_links = ('pk', 'title')
    ordering = ('pk',)
    list_per_page = 10

    list_filter = ('status', 'created_at')
    search_fields = ('title',)


    def description_short(self, obj:Task):
        if len(obj.description) < 32:
            return obj.description
        return obj.description[:32] + '...'

    description_short.short_description = 'Описание'

