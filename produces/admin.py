from django.contrib import admin
from .models import Produce

@admin.register(Produce)

class ProduceAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'price',
        'market',
        'farmer',
        'quantity_available',
        'date_added'
    )

    list_filter = ('market', 'farmer', 'price',  'date_added')
    search_fields = ('name', 'farmer__email', 'market__name')
    ordering = ('-date_added',)

    readonly_fields = ('date_added', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Quantity', {
            'fields': ('price', 'quantity_available')
        }),
        ('Relationships', {
            'fields': ('market', 'farmer')
        }),
        ('Timestamps', {
            'fields': ('date_added', 'updated_at')
        }),
    )

