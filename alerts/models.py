from django.db import models
from produces.models import Produce
from markets.models import Market
from django.conf import settings


class PriceAlert(models.Model):
    ALERT_TYPES = (
        ('threshold', 'Threshold'),
        ('all_changes', 'All Changes'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='price_alerts'
    )
    produce = models.ForeignKey(
        Produce,
        on_delete=models.CASCADE,
        related_name="produce_alerts"
    )
    
    threshold_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    
    alert_type = models.CharField(
        max_length=20,
        choices=ALERT_TYPES,
        default="threshold",
    )
    
    created_at  = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.email} - {self.produce.name}"
    
