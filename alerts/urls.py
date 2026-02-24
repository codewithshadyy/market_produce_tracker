from rest_framework.routers import DefaultRouter
from .views import PriceAlertViewSet

router = DefaultRouter()
router.register(r'alerts', PriceAlertViewSet, basename='alerts')

urlpatterns = router.urls