from django.contrib import admin

from .models import Market

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):

    list_display = ('name', 'location', 'created_by', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('name', 'location', 'created_by__email')
    ordering = ('-created_at',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Market Info', {
            'fields': ('name', 'location')
        }),
        ('Ownership', {
            'fields': ('created_by',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
