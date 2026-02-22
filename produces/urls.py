

from rest_framework.routers import DefaultRouter
from .views import ProduceViewSet
from django.urls import path

router = DefaultRouter()
router.register(r"produce", ProduceViewSet )
urlpatterns = router.urls

