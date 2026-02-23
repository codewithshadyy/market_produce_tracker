from django.contrib import admin

from .models import PriceAlert
@admin.register(PriceAlert)

class AdminPriceAlert(admin.ModelAdmin):
    list_display = (
       "produce",
            "threshold_price",
            "alert_type",
            "created_at"
        
    )

