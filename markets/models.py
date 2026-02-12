from django.db import models
from django.conf import settings


class Market(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="markets"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
     
    
    def __str__(self):
        return f"{self.name}-{self.location}"
