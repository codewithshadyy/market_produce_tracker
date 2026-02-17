from django.shortcuts import render
from  .models import Produce
from rest_framework import viewsets
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
    
    
    def get_permissions(self):
        if self.action == "create":
            return[IsFarmerOrAdmin()] 
        
        elif self.action in ["update", "partial_update", "destroy"]:
            return[IsFarmerOrAdmin(), IsOwnerOrAdmin()]
        
        return[IsAuthenticatedOrReadOnly()]
    def perform_create(self, serializer):
        return serializer.save(farmer = self.request.user)
    

