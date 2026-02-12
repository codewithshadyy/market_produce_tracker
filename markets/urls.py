from rest_framework.routers import DefaultRouter
from .views import MarketViewSet


router = DefaultRouter()

router.register(r"markets", MarketViewSet)

urlpatterns = router.urls
