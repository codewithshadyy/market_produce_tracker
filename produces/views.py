from django.shortcuts import render
from  .models import Produce,PriceHistory
from alerts.models import PriceAlert
from rest_framework import viewsets,serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ProduceSerializer
from .permissions import IsFarmerOrAdmin, IsOwnerOrAdmin
from config.pagination import CustomPagination


class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['market', 'farmer']
    search_fields = ['name']
    ordering_fields = ['price']
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    def get_permissions(self):
        if self.action == "create":
            return[IsFarmerOrAdmin()] 
        
        elif self.action in ["update", "partial_update", "destroy"]:
            return[IsFarmerOrAdmin(), IsOwnerOrAdmin()]
        
        return[IsAuthenticatedOrReadOnly()]
    def perform_create(self, serializer):
        return serializer.save(farmer = self.request.user)
    
    
    def perform_update(self, serializer):
     instance = self.get_object()
     old_price = instance.price

     updated_instance = serializer.save()

     if old_price != updated_instance.price:
        # Save price history
        PriceHistory.objects.create(
            produce=updated_instance,
            old_price=old_price,
            new_price=updated_instance.price
        )

        # Trigger alerts
        alerts = PriceAlert.objects.filter(
            produce=updated_instance,
            is_triggered=False
        )

        for alert in alerts:
            if (
                alert.alert_type == "ABOVE" and
                updated_instance.price > alert.threshold_price
            ) or (
                alert.alert_type == "BELOW" and
                updated_instance.price < alert.threshold_price
            ):
                alert.is_triggered = True
                alert.save()
    


