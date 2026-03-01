
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
    old_instance = Produce.objects.get(pk=instance.pk)
    
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
              subject = f"Threshold price reacheed!!!" ,
              message= ( f"Hello {alert.user.username}, The price of {alert.produce.name} at {alert.produce.market} market by {alert.produce.farmer} " 
               f" has reached {alert.threshold_price}, which surpasses your threshold of {alert.produce.price}.\n\n" 
               f"Regards,\nIntegrity market"),
              from_email="kipkoechshadrack@gmail.com",
              recipient_list=[alert.user.email]
            )
            
    elif alert.alert_type == "all_changes":
        send_mail(
            subject="Price Updated",
            message=f"Price of {alert.produce.name} changed from {old_price} to {new_price}",
            from_email="kipkoechshadrack10@gmail.com",
            recipient_list=[alert.user.email],
            
        )  
          
            
    