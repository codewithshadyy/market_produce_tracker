from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ROLE_CHOICES =  (
        ('ADMIN', 'Admin'),
        ('FARMER', 'Farmer'),
        ('CLIENT', 'Client'),
    )
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="CLIENT")
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    allowed_markets = models.ManyToManyField(
    "markets.Market",
    blank=True,
    related_name="allowed_farmers"
)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email
    
