
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import(
    IsAuthenticatedOrReadOnly, 
    IsAuthenticated,
    IsAdminUser
    )
from .serializers import MarketSerializer
from .permissions import IsAdminOrReadOnly

from .models import Market

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_permissions(self): 
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)