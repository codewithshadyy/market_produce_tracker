
from django.dispatch import receiver
from django.db.models.signals import pre_save
from produces.models import Produce
from .models import PriceAlert
from django.core.mail import send_mail
from django.conf import settings

@receiver(pre_save, sender=Produce)

def check_price_change(sender, instance, **kwargs):
    
    if  not instance.pk:
        return
    old_instance = Produce.objects.filter(pk=instance.pk)
    
    if old_instance.price == instance.price:
        return
    
    alerts = PriceAlert.objects.filter(produce=instance).select_related("user")   
    
    for alert in alerts:
        send_notification(alert, old_instance.price, instance.price)
        

def  send_notification(alert, old_price, new_price):
    
    if alert.alert_type == "threshold":
        if alert.threshold_price is None:
            return
        if new_price <= alert.threshold_price:
            
            send_mail(
               f"Hello,\n\n" 
               f"The price of {Produce.name} at {Produce.market.name} " 
               f"has reached {Produce.price}, which surpasses your threshold of {alert.threshold_price}.\n\n" 
               f"Regards,\nMarket Alerts System"
            )
            
    elif alert.alert_type == "all_changes":
        send_mail(
            subject="Price Updated",
            message=f"Price changed from {old_price} to {new_price}",
            from_email="integritymarket@gmil.com",
            recipient_list=[alert.user.email]
        )  
          
            
    