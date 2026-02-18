

from django.urls import path
from . import views

urlpatterns = [
    path("price-alert/", views.PriceAlertViewSet.as_view({'get':'list'}), name="price_alert")
]


