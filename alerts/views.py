from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import PriceAlert
from .serializers import PriceAlertSerializer
from config.pagination import CustomPagination

class PriceAlertViewSet(ModelViewSet):
    serializer_class = PriceAlertSerializer
    permission_classes = [IsAuthenticated]
    queryset = PriceAlert.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        return PriceAlert.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


