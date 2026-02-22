from django.db import models
from django.conf import settings
from markets.models import Market


class Produce(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="produces")
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="produces")
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}-{self.price}-{self.farmer}-{self.market}"
    

class PriceHistory(models.Model):
    produce = models.ForeignKey(  Produce,
        on_delete=models.CASCADE,
        related_name="price_history")
    
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    changed_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.produce.name} changed from {self.old_price} to {self.new_price}"  

